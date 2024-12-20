class DanteSubscription:
    def __init__(self):
        self._error = None
        self._rx_channel = None
        self._rx_channel_name = None
        self._rx_device = None
        self._rx_device_name = None
        self._status_code = None
        self._tx_channel = None
        self._tx_channel_name = None
        self._tx_device = None
        self._tx_device_name = None

    @property
    def error(self):
        return self._error

    @error.setter
    def error(self, error):
        self._error = error

    def __str__(self):
        if self.tx_channel_name and self.tx_device_name:
            text = f"{self.rx_channel_name}@{self.rx_device_name} <- {self.tx_channel_name}@{self.tx_device_name}"
        else:
            text = f"{self.rx_channel_name}@{self.rx_device_name}"
        return text

    @property
    def rx_channel(self):
        return self._rx_channel

    @rx_channel.setter
    def rx_channel(self, rx_channel):
        self._rx_channel = rx_channel

    @property
    def rx_channel_name(self):
        return self._rx_channel_name

    @rx_channel_name.setter
    def rx_channel_name(self, rx_channel_name):
        self._rx_channel_name = rx_channel_name

    @property
    def rx_device(self):
        return self._rx_device

    @rx_device.setter
    def rx_device(self, rx_device):
        self._rx_device = rx_device

    @property
    def rx_device_name(self):
        return self._rx_device_name

    @rx_device_name.setter
    def rx_device_name(self, rx_device_name):
        self._rx_device_name = rx_device_name

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        self._status_code = status_code

    @property
    def tx_channel(self):
        return self._tx_channel

    @tx_channel.setter
    def tx_channel(self, tx_channel):
        self._tx_channel = tx_channel

    @property
    def tx_channel_name(self):
        return self._tx_channel_name

    @tx_channel_name.setter
    def tx_channel_name(self, tx_channel_name):
        self._tx_channel_name = tx_channel_name

    @property
    def tx_device(self):
        return self._tx_device

    @tx_device.setter
    def tx_device(self, tx_device):
        self._tx_device = tx_device

    @property
    def tx_device_name(self):
        return self._tx_device_name

    @tx_device_name.setter
    def tx_device_name(self, tx_device_name):
        self._tx_device_name = tx_device_name

    def to_json(self):
        return {
            "rx_channel": self.rx_channel_name,
            "rx_device": self.rx_device_name,
            "tx_channel": self.tx_channel_name,
            "tx_device": self.tx_device_name,
        }
