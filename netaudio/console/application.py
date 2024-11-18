import os
from cleo.application import Application
from netaudio import version

from netaudio.console.commands import (
    ChannelCommand,
    ConfigCommand,
    DeviceCommand,
    ServerCommand,
    SubscriptionCommand,
)

# Only import and use signal handling on Unix-like systems
if os.name != "nt":  # not Windows
    from signal import signal, SIGPIPE, SIG_DFL
    signal(SIGPIPE, SIG_DFL)


def main() -> int:
    commands = [
        ChannelCommand,
        ConfigCommand,
        DeviceCommand,
        ServerCommand,
        SubscriptionCommand,
    ]

    application = Application("netaudio", version.version)

    for command in commands:
        application.add(command())

    return application.run()


if __name__ == "__main__":
    main()
