import asyncio
import json
import os

from json import JSONEncoder

from cleo.commands.command import Command
from cleo.helpers import option
from redis import Redis
from redis.exceptions import ConnectionError as RedisConnectionError

from netaudio.dante.browser import DanteBrowser

# from netaudio.dante.cache import DanteCache


def _default(self, obj):
    return getattr(obj.__class__, "to_json", _default.default)(obj)


_default.default = JSONEncoder().default
JSONEncoder.default = _default


class SubscriptionListCommand(Command):
    name = "list"
    description = "List subscriptions"

    options = [
        option("json", None, "Output as JSON", flag=True),
        option("rx-channel-name", None, "Filter by Rx channel name", flag=False),
        option("rx-channel-number", None, "Filter by Rx channel number", flag=False),
        option("rx-device-host", None, "Filter by Rx device host", flag=False),
        option("rx-device-name", None, "Filter by Rx device name", flag=False),
        option("tx-channel-name", None, "Filter by Tx channel name", flag=False),
        option("tx-channel-number", None, "Filter by Tx channel number", flag=False),
        option("tx-device-host", None, "Filter by Tx device host", flag=False),
        option("tx-device-name", None, "Filter by Tx device name", flag=False),
    ]

    async def subscription_list(self):
        subscriptions = []

        redis_enabled = None

        redis_socket_path = os.environ.get("REDIS_SOCKET")
        redis_host = os.environ.get("REDIS_HOST") or "localhost"
        redis_port = os.environ.get("REDIS_PORT") or 6379
        redis_db = os.environ.get("REDIS_DB") or 0

        try:
            redis_client = None

            if redis_socket_path:
                redis_client = Redis(
                    db=redis_db,
                    decode_responses=False,
                    socket_timeout=0.1,
                    unix_socket_path=redis_socket_path,
                )
            elif os.environ.get("REDIS_PORT") or os.environ.get("REDIS_HOST"):
                redis_client = Redis(
                    db=redis_db,
                    decode_responses=False,
                    host=redis_host,
                    socket_timeout=0.1,
                    port=redis_port,
                )
            if redis_client:
                redis_client.ping()
                redis_enabled = True
        except RedisConnectionError:
            redis_enabled = False

        if redis_enabled:
            # dante_cache = DanteCache()
            devices = await dante_cache.get_devices()
            devices = dict(sorted(devices.items(), key=lambda x: x[1].name))
        else:
            dante_browser = DanteBrowser(mdns_timeout=1.5)
            devices = await dante_browser.get_devices()
            devices = dict(sorted(devices.items(), key=lambda x: x[1].name))

            for _, device in devices.items():
                await device.get_controls()

        # Get filter criteria
        rx_device = None
        tx_device = None

        if self.option("rx-device-name"):
            try:
                rx_device = next(filter(lambda d: d[1].name == self.option("rx-device-name"), devices.items()))[1]
            except StopIteration:
                self.line(f"<error>Rx device '{self.option('rx-device-name')}' not found</error>")
                return
        elif self.option("rx-device-host"):
            try:
                rx_device = next(filter(lambda d: d[1].ipv4 == self.option("rx-device-host"), devices.items()))[1]
            except StopIteration:
                self.line(f"<error>Rx device with host '{self.option('rx-device-host')}' not found</error>")
                return

        if self.option("tx-device-name"):
            try:
                tx_device = next(filter(lambda d: d[1].name == self.option("tx-device-name"), devices.items()))[1]
            except StopIteration:
                self.line(f"<error>Tx device '{self.option('tx-device-name')}' not found</error>")
                return
        elif self.option("tx-device-host"):
            try:
                tx_device = next(filter(lambda d: d[1].ipv4 == self.option("tx-device-host"), devices.items()))[1]
            except StopIteration:
                self.line(f"<error>Tx device with host '{self.option('tx-device-host')}' not found</error>")
                return

        # Collect subscriptions with filtering
        for _, device in devices.items():
            for subscription in device.subscriptions:
                # Apply filters
                if rx_device and subscription.rx_device_name != rx_device.name:
                    continue
                
                if tx_device and subscription.tx_device_name != tx_device.name:
                    continue

                if self.option("rx-channel-name") and subscription.rx_channel_name != self.option("rx-channel-name"):
                    continue

                if self.option("tx-channel-name") and subscription.tx_channel_name != self.option("tx-channel-name"):
                    continue

                if self.option("rx-channel-number"):
                    try:
                        if str(subscription.rx_channel_number) != str(self.option("rx-channel-number")):
                            continue
                    except AttributeError:
                        continue

                if self.option("tx-channel-number"):
                    try:
                        if str(subscription.tx_channel_number) != str(self.option("tx-channel-number")):
                            continue
                    except AttributeError:
                        continue

                subscriptions.append(subscription)

        if not subscriptions:
            self.line("<comment>No matching subscriptions found</comment>")
            return

        if self.option("json"):
            json_object = json.dumps(subscriptions, indent=2)
            self.line(f"{json_object}")
        else:
            for subscription in subscriptions:
                self.line(f"{subscription}")

    def handle(self):
        asyncio.run(self.subscription_list())
