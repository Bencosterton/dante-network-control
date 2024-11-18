SERVICE_ARC: str = "_netaudio-arc._udp.local."
SERVICE_CHAN: str = "_netaudio-chan._udp.local."
SERVICE_CMC: str = "_netaudio-cmc._udp.local."
SERVICE_DBC: str = "_netaudio-dbc._udp.local."

MULTICAST_GROUP_HEARTBEAT = "224.0.0.233"
MULTICAST_GROUP_CONTROL_MONITORING = "224.0.0.231"

SERVICES = [SERVICE_ARC, SERVICE_CHAN, SERVICE_CMC, SERVICE_DBC]

FEATURE_VOLUME_UNSUPPORTED = [
    "DAI1",
    "DAI2",
    "DAO1",
    "DAO2",
    "DIAES3",
    "DIOUSB",
    "DIUSBC",
    "_86012780000a0003",
]

DEFAULT_MULTICAST_METERING_PORT = 8751
DEVICE_CONTROL_PORT: int = 8800
DEVICE_HEARTBEAT_PORT: int = 8708
DEVICE_INFO_PORT: int = 8702
DEVICE_INFO_SRC_PORT1 = 1029
DEVICE_INFO_SRC_PORT2 = 1030
DEVICE_SETTINGS_PORT: int = 8700
MESSAGE_TYPE_VOLUME_LEVELS = 0

PORTS = [DEVICE_CONTROL_PORT, DEVICE_INFO_PORT, DEVICE_SETTINGS_PORT]

SUBSCRIPTION_STATUS_BUNDLE_FORMAT = 17
SUBSCRIPTION_STATUS_CHANNEL_FORMAT = 16
SUBSCRIPTION_STATUS_CHANNEL_LATENCY = 26
SUBSCRIPTION_STATUS_CLOCK_DOMAIN = 27
SUBSCRIPTION_STATUS_DYNAMIC = 9
SUBSCRIPTION_STATUS_DYNAMIC_PROTOCOL = 31
SUBSCRIPTION_STATUS_FLAG_NO_ADVERT = 256
SUBSCRIPTION_STATUS_FLAG_NO_DBCP = 512
SUBSCRIPTION_STATUS_HDCP_NEGOTIATION_ERROR = 112
SUBSCRIPTION_STATUS_IDLE = 7
SUBSCRIPTION_STATUS_INVALID_CHANNEL = 32
SUBSCRIPTION_STATUS_INVALID_MSG = 25
SUBSCRIPTION_STATUS_IN_PROGRESS = 8
SUBSCRIPTION_STATUS_MANUAL = 14
SUBSCRIPTION_STATUS_NONE = 0
SUBSCRIPTION_STATUS_NO_CONNECTION = 15
SUBSCRIPTION_STATUS_NO_DATA = 65536
SUBSCRIPTION_STATUS_NO_RX = 18
SUBSCRIPTION_STATUS_NO_TX = 20
SUBSCRIPTION_STATUS_QOS_FAIL_RX = 22
SUBSCRIPTION_STATUS_QOS_FAIL_TX = 23
SUBSCRIPTION_STATUS_RESOLVED = 2
SUBSCRIPTION_STATUS_RESOLVED_NONE = 5
SUBSCRIPTION_STATUS_RESOLVE_FAIL = 3
SUBSCRIPTION_STATUS_RX_FAIL = 19
SUBSCRIPTION_STATUS_RX_LINK_DOWN = 29
SUBSCRIPTION_STATUS_RX_NOT_READY = 36
SUBSCRIPTION_STATUS_RX_UNSUPPORTED_SUB_MODE = 69
SUBSCRIPTION_STATUS_STATIC = 10
SUBSCRIPTION_STATUS_SUBSCRIBE_SELF = 4
SUBSCRIPTION_STATUS_SUBSCRIBE_SELF_POLICY = 34
SUBSCRIPTION_STATUS_SYSTEM_FAIL = 255
SUBSCRIPTION_STATUS_TEMPLATE_FULL = 68
SUBSCRIPTION_STATUS_TEMPLATE_MISMATCH_CONFIG = 67
SUBSCRIPTION_STATUS_TEMPLATE_MISMATCH_DEVICE = 64
SUBSCRIPTION_STATUS_TEMPLATE_MISMATCH_FORMAT = 65
SUBSCRIPTION_STATUS_TEMPLATE_MISSING_CHANNEL = 66
SUBSCRIPTION_STATUS_TX_ACCESS_CONTROL_DENIED = 96
SUBSCRIPTION_STATUS_TX_ACCESS_CONTROL_PENDING = 97
SUBSCRIPTION_STATUS_TX_CHANNEL_ENCRYPTED = 38
SUBSCRIPTION_STATUS_TX_FAIL = 21
SUBSCRIPTION_STATUS_TX_FANOUT_LIMIT_REACHED = 37
SUBSCRIPTION_STATUS_TX_LINK_DOWN = 30
SUBSCRIPTION_STATUS_TX_NOT_READY = 35
SUBSCRIPTION_STATUS_TX_REJECTED_ADDR = 24
SUBSCRIPTION_STATUS_TX_RESPONSE_UNEXPECTED = 39
SUBSCRIPTION_STATUS_TX_SCHEDULER_FAILURE = 33
SUBSCRIPTION_STATUS_TX_UNSUPPORTED_SUB_MODE = 70
SUBSCRIPTION_STATUS_UNRESOLVED = 1
SUBSCRIPTION_STATUS_UNSUPPORTED = 28

SUBSCRIPTION_STATUSES = [
    SUBSCRIPTION_STATUS_BUNDLE_FORMAT,
    SUBSCRIPTION_STATUS_CHANNEL_FORMAT,
    SUBSCRIPTION_STATUS_CHANNEL_LATENCY,
    SUBSCRIPTION_STATUS_CLOCK_DOMAIN,
    SUBSCRIPTION_STATUS_DYNAMIC,
    SUBSCRIPTION_STATUS_DYNAMIC_PROTOCOL,
    SUBSCRIPTION_STATUS_FLAG_NO_ADVERT,
    SUBSCRIPTION_STATUS_FLAG_NO_DBCP,
    SUBSCRIPTION_STATUS_HDCP_NEGOTIATION_ERROR,
    SUBSCRIPTION_STATUS_IDLE,
    SUBSCRIPTION_STATUS_INVALID_CHANNEL,
    SUBSCRIPTION_STATUS_INVALID_MSG,
    SUBSCRIPTION_STATUS_IN_PROGRESS,
    SUBSCRIPTION_STATUS_MANUAL,
    SUBSCRIPTION_STATUS_NONE,
    SUBSCRIPTION_STATUS_NO_CONNECTION,
    SUBSCRIPTION_STATUS_NO_DATA,
    SUBSCRIPTION_STATUS_NO_RX,
    SUBSCRIPTION_STATUS_NO_TX,
    SUBSCRIPTION_STATUS_QOS_FAIL_RX,
    SUBSCRIPTION_STATUS_QOS_FAIL_TX,
    SUBSCRIPTION_STATUS_RESOLVED,
    SUBSCRIPTION_STATUS_RESOLVED_NONE,
    SUBSCRIPTION_STATUS_RESOLVE_FAIL,
    SUBSCRIPTION_STATUS_RX_FAIL,
    SUBSCRIPTION_STATUS_RX_LINK_DOWN,
    SUBSCRIPTION_STATUS_RX_NOT_READY,
    SUBSCRIPTION_STATUS_RX_UNSUPPORTED_SUB_MODE,
    SUBSCRIPTION_STATUS_STATIC,
    SUBSCRIPTION_STATUS_SUBSCRIBE_SELF,
    SUBSCRIPTION_STATUS_SUBSCRIBE_SELF_POLICY,
    SUBSCRIPTION_STATUS_SYSTEM_FAIL,
    SUBSCRIPTION_STATUS_TEMPLATE_FULL,
    SUBSCRIPTION_STATUS_TEMPLATE_MISMATCH_CONFIG,
    SUBSCRIPTION_STATUS_TEMPLATE_MISMATCH_DEVICE,
    SUBSCRIPTION_STATUS_TEMPLATE_MISMATCH_FORMAT,
    SUBSCRIPTION_STATUS_TEMPLATE_MISSING_CHANNEL,
    SUBSCRIPTION_STATUS_TX_ACCESS_CONTROL_DENIED,
    SUBSCRIPTION_STATUS_TX_ACCESS_CONTROL_PENDING,
    SUBSCRIPTION_STATUS_TX_CHANNEL_ENCRYPTED,
    SUBSCRIPTION_STATUS_TX_FAIL,
    SUBSCRIPTION_STATUS_TX_FANOUT_LIMIT_REACHED,
    SUBSCRIPTION_STATUS_TX_LINK_DOWN,
    SUBSCRIPTION_STATUS_TX_NOT_READY,
    SUBSCRIPTION_STATUS_TX_REJECTED_ADDR,
    SUBSCRIPTION_STATUS_TX_RESPONSE_UNEXPECTED,
    SUBSCRIPTION_STATUS_TX_SCHEDULER_FAILURE,
    SUBSCRIPTION_STATUS_TX_UNSUPPORTED_SUB_MODE,
    SUBSCRIPTION_STATUS_UNRESOLVED,
    SUBSCRIPTION_STATUS_UNSUPPORTED,
]

SUBSCRIPTION_STATUS_LABELS = {
    SUBSCRIPTION_STATUS_NONE: ("none", "No subscription for this channel"),
    SUBSCRIPTION_STATUS_FLAG_NO_ADVERT: ("No audio data.",),
    SUBSCRIPTION_STATUS_UNRESOLVED: (
        "Subscription unresolved",
        "Unresolved",
        "cannot find this channel on the network",
    ),
    SUBSCRIPTION_STATUS_RESOLVED: (
        "Subscription resolved",
        "Resolved",
        "channel found; preparing to create flow",
    ),
    SUBSCRIPTION_STATUS_UNRESOLVED: (
        "Unresolved: channel not present",
        "Unresolved",
        "this channel is not present on the network",
    ),
    SUBSCRIPTION_STATUS_RESOLVE_FAIL: (
        "Can't resolve subscription",
        "Resolve failed",
        "received an unexpected error when trying to resolve this channel",
    ),
    SUBSCRIPTION_STATUS_SUBSCRIBE_SELF: (
        "Subscribed to own signal",
        "Connected (self)",
    ),
    SUBSCRIPTION_STATUS_IDLE: (
        "Subscription idle",
        "Flow creation idle",
        "Insufficient information to create flow",
    ),
    SUBSCRIPTION_STATUS_IN_PROGRESS: (
        "Subscription in progress",
        "Flow creation in progress",
        "communicating with transmitter to create flow",
    ),
    SUBSCRIPTION_STATUS_DYNAMIC: ("Connected (unicast)",),
    SUBSCRIPTION_STATUS_STATIC: ("Connected (multicast)",),
    SUBSCRIPTION_STATUS_MANUAL: ("Manually Configured",),
    SUBSCRIPTION_STATUS_NO_CONNECTION: (
        "No connection",
        "could not communicate with transmitter",
    ),
    SUBSCRIPTION_STATUS_CHANNEL_FORMAT: (
        "Incorrect channel format",
        "source and destination channels do not match",
    ),
    SUBSCRIPTION_STATUS_BUNDLE_FORMAT: (
        "Incorrect flow format",
        "Incorrect multicast flow format",
        "flow format incompatible with receiver",
    ),
    SUBSCRIPTION_STATUS_NO_RX: (
        "No Receive flows",
        "No more flows (RX)",
        "receiver cannot support any more flows",
        "Is receiver subscribed to too many different devices?",
    ),
    SUBSCRIPTION_STATUS_RX_FAIL: (
        "Receive failure",
        "Receiver setup failed",
        "unexpected error on receiver",
    ),
    SUBSCRIPTION_STATUS_NO_TX: (
        "No Transmit flows",
        "No more flows (TX)",
        "transmitter cannot support any more flows",
        "Reduce fan out by unsubscribing receivers or switching to multicast.",
    ),
    SUBSCRIPTION_STATUS_TX_FAIL: (
        "Transmit failure",
        "Transmitter setup failed",
        "unexpected error on transmitter",
    ),
    SUBSCRIPTION_STATUS_QOS_FAIL_RX: (
        "Receive bandwidth exceeded",
        "receiver can't reliably support any more inbound flows",
        "Reduce number of subscriptions or look for excessive multicast.",
    ),
    SUBSCRIPTION_STATUS_QOS_FAIL_TX: (
        "Transmit bandwidth exceeded",
        "transmitter can't reliably support any more outbound flows",
        "Reduce fan out by unsubscribing receivers or switching to multicast.",
    ),
    SUBSCRIPTION_STATUS_TX_REJECTED_ADDR: (
        "Subscription address rejected by transmitter",
        "Transmitter rejected address",
        "transmitter can't talk to receiver's address",
        "Check for address change on transmitter or receiver.",
    ),
    SUBSCRIPTION_STATUS_INVALID_MSG: (
        "Subscription message rejected by transmitter",
        "Transmitter rejected message",
        "transmitter can't understand receiver's request",
    ),
    SUBSCRIPTION_STATUS_CHANNEL_LATENCY: (
        "No suitable channel latency",
        "Incorrect channel latencies",
        "source demands more latency than the receiver has available",
    ),
    SUBSCRIPTION_STATUS_CLOCK_DOMAIN: (
        "Mismatched clock domains",
        "The transmitter and receiver are not part of the same clock domain",
    ),
    SUBSCRIPTION_STATUS_UNSUPPORTED: (
        "Unsupported feature",
        "The subscription cannot be completed as it requires features that are not supported on this device",
    ),
    SUBSCRIPTION_STATUS_RX_LINK_DOWN: (
        "RX link down",
        "RX link down",
        "The subscription cannot be completed as RX link is down",
    ),
    SUBSCRIPTION_STATUS_TX_LINK_DOWN: (
        "TX link down",
        "The subscription cannot be completed as TX link is down",
    ),
    SUBSCRIPTION_STATUS_DYNAMIC_PROTOCOL: ("Dynamic Protocol",),
    SUBSCRIPTION_STATUS_INVALID_CHANNEL: (
        "Invalid Channel",
        "the subscription cannot be completed as channel is invalid",
    ),
    SUBSCRIPTION_STATUS_TEMPLATE_MISMATCH_DEVICE: (
        "The receive channel's subscription does not match the templates TX device",
        "Template mismatch (device)",
    ),
    SUBSCRIPTION_STATUS_TEMPLATE_MISMATCH_FORMAT: (
        "The receive channel's available audio formats do not match the template's audio format",
        "Template mismatch (format)",
    ),
    SUBSCRIPTION_STATUS_TEMPLATE_MISSING_CHANNEL: (
        "The receive channel's subscription is not a part of the given multicast template",
        "Template missing channel",
    ),
    SUBSCRIPTION_STATUS_TEMPLATE_MISMATCH_CONFIG: (
        "The receive channel's resolved information conflicts with the multicast templates resolved information",
        "Template mismatch (config)",
    ),
    SUBSCRIPTION_STATUS_TEMPLATE_FULL: (
        "The receive channel's template is already full",
        "Template full",
    ),
    SUBSCRIPTION_STATUS_SYSTEM_FAIL: (
        "System failure",
        "Incorrect multicast flow format",
        "flow format incompatible with receiver",
    ),
    SUBSCRIPTION_STATUS_TX_SCHEDULER_FAILURE: (
        "TX Scheduler failure",
        "This is most often caused by a receiver with  < 1ms unicast latency subscribing to a transmitter on a 100MB connection",
    ),
    SUBSCRIPTION_STATUS_SUBSCRIBE_SELF_POLICY: (
        "Subscription to own signal disallowed by device",
        "Policy failure for subscription to self",
        "The device does not support local subscriptions for the given transmit and receive channels.",
    ),
}


REQUEST_DANTE_MODEL = 97
REQUEST_MAKE_MODEL = 193
RESPONSE_DANTE_MODEL = 96
RESPONSE_MAKE_MODEL = 192


MESSAGE_TYPE_CHANNEL_COUNTS_QUERY = 4096
MESSAGE_TYPE_DEVICE_CONTROL = 4099
MESSAGE_TYPE_IDENTIFY_DEVICE_QUERY = 4302
MESSAGE_TYPE_NAME_CONTROL = 4097
MESSAGE_TYPE_NAME_QUERY = 4098
MESSAGE_TYPE_RX_CHANNEL_QUERY = 12288
MESSAGE_TYPE_TX_CHANNEL_QUERY = 8192
MESSAGE_TYPE_TX_CHANNEL_FRIENDLY_NAMES_QUERY = 8208

MESSAGE_TYPE_ACCESS_CONTROL = 177
MESSAGE_TYPE_ACCESS_STATUS = 176
MESSAGE_TYPE_AES67_CONTROL = 4102
MESSAGE_TYPE_AES67_STATUS = 4103
MESSAGE_TYPE_AUDIO_INTERFACE_QUERY = 135
MESSAGE_TYPE_AUDIO_INTERFACE_STATUS = 134
MESSAGE_TYPE_CLEAR_CONFIG_CONTROL = 119
MESSAGE_TYPE_CLEAR_CONFIG_STATUS = 120
MESSAGE_TYPE_CLOCKING_CONTROL = 33
MESSAGE_TYPE_CLOCKING_STATUS = 32
MESSAGE_TYPE_CODEC_CONTROL = 4106
MESSAGE_TYPE_CODEC_STATUS = 4107
MESSAGE_TYPE_CONFIG_CONTROL = 115
MESSAGE_TYPE_DDM_ENROLMENT_CONFIG_CONTROL = 65286
MESSAGE_TYPE_DDM_ENROLMENT_CONFIG_STATUS = 65287
MESSAGE_TYPE_DEVICE_REBOOT = 146
MESSAGE_TYPE_EDK_BOARD_CONTROL = 161
MESSAGE_TYPE_EDK_BOARD_STATUS = 160
MESSAGE_TYPE_ENCODING_CONTROL = 131
MESSAGE_TYPE_ENCODING_STATUS = 130
MESSAGE_TYPE_HAREMOTE_CONTROL = 4097
MESSAGE_TYPE_HAREMOTE_STATUS = 4096
MESSAGE_TYPE_IDENTIFY_QUERY = 99
MESSAGE_TYPE_IDENTIFY_STATUS = 98
MESSAGE_TYPE_IFSTATS_QUERY = 65
MESSAGE_TYPE_IFSTATS_STATUS = 64
MESSAGE_TYPE_IGMP_VERS_CONTROL = 81
MESSAGE_TYPE_IGMP_VERS_STATUS = 80
MESSAGE_TYPE_INTERFACE_CONTROL = 19
MESSAGE_TYPE_INTERFACE_STATUS = 17
MESSAGE_TYPE_LED_QUERY = 209
MESSAGE_TYPE_LED_STATUS = 208
MESSAGE_TYPE_LOCK_QUERY = 4104
MESSAGE_TYPE_LOCK_STATUS = 4105
MESSAGE_TYPE_MANF_VERSIONS_QUERY = 193
MESSAGE_TYPE_MANF_VERSIONS_STATUS = 192
MESSAGE_TYPE_MASTER_QUERY = 35
MESSAGE_TYPE_MASTER_STATUS = 34
MESSAGE_TYPE_METERING_CONTROL = 225
MESSAGE_TYPE_METERING_STATUS = 224
MESSAGE_TYPE_NAME_ID_CONTROL = 39
MESSAGE_TYPE_NAME_ID_STATUS = 38
MESSAGE_TYPE_PROPERTY_CHANGE = 262
MESSAGE_TYPE_ROUTING_DEVICE_CHANGE = 288
MESSAGE_TYPE_ROUTING_READY = 256
MESSAGE_TYPE_RX_CHANNEL_CHANGE = 258
MESSAGE_TYPE_RX_CHANNEL_RX_ERROR_QUERY = 273
MESSAGE_TYPE_RX_CHANNEL_RX_ERROR_STATUS = 272
MESSAGE_TYPE_RX_ERROR_THRESHOLD_CONTROL = 275
MESSAGE_TYPE_RX_ERROR_THRESHOLD_STATUS = 274
MESSAGE_TYPE_RX_FLOW_CHANGE = 261
MESSAGE_TYPE_SAMPLE_RATE_CONTROL = 129
MESSAGE_TYPE_SAMPLE_RATE_PULLUP_CONTROL = 133
MESSAGE_TYPE_SAMPLE_RATE_PULLUP_STATUS = 132
MESSAGE_TYPE_SAMPLE_RATE_STATUS = 128
MESSAGE_TYPE_SERIAL_PORT_CONTROL = 241
MESSAGE_TYPE_SERIAL_PORT_STATUS = 240
MESSAGE_TYPE_SWITCH_VLAN_CONTROL = 21
MESSAGE_TYPE_SWITCH_VLAN_STATUS = 20
MESSAGE_TYPE_SYS_RESET = 144
MESSAGE_TYPE_TOPOLOGY_CHANGE = 16
MESSAGE_TYPE_TX_CHANNEL_CHANGE = 257
MESSAGE_TYPE_TX_FLOW_CHANGE = 260
MESSAGE_TYPE_TX_LABEL_CHANGE = 259
MESSAGE_TYPE_UNICAST_CLOCKING_CONTROL = 37
MESSAGE_TYPE_UNICAST_CLOCKING_STATUS = 36
MESSAGE_TYPE_UPGRADE_CONTROL = 113
MESSAGE_TYPE_UPGRADE_STATUS = 112
MESSAGE_TYPE_VERSIONS_QUERY = 97
MESSAGE_TYPE_VERSIONS_STATUS = 96

MESSAGE_TYPE_STATUS = [
    MESSAGE_TYPE_ACCESS_STATUS,
    MESSAGE_TYPE_AES67_STATUS,
    MESSAGE_TYPE_AUDIO_INTERFACE_STATUS,
    MESSAGE_TYPE_CLEAR_CONFIG_STATUS,
    MESSAGE_TYPE_CLOCKING_STATUS,
    MESSAGE_TYPE_CODEC_STATUS,
    MESSAGE_TYPE_DDM_ENROLMENT_CONFIG_STATUS,
    MESSAGE_TYPE_EDK_BOARD_STATUS,
    MESSAGE_TYPE_ENCODING_STATUS,
    MESSAGE_TYPE_HAREMOTE_STATUS,
    MESSAGE_TYPE_IDENTIFY_STATUS,
    MESSAGE_TYPE_IFSTATS_STATUS,
    MESSAGE_TYPE_IGMP_VERS_STATUS,
    MESSAGE_TYPE_INTERFACE_STATUS,
    MESSAGE_TYPE_LED_STATUS,
    MESSAGE_TYPE_LOCK_STATUS,
    MESSAGE_TYPE_MANF_VERSIONS_STATUS,
    MESSAGE_TYPE_MASTER_STATUS,
    MESSAGE_TYPE_METERING_STATUS,
    MESSAGE_TYPE_NAME_ID_STATUS,
    MESSAGE_TYPE_RX_CHANNEL_RX_ERROR_STATUS,
    MESSAGE_TYPE_RX_ERROR_THRESHOLD_STATUS,
    MESSAGE_TYPE_SAMPLE_RATE_PULLUP_STATUS,
    MESSAGE_TYPE_SAMPLE_RATE_STATUS,
    MESSAGE_TYPE_SERIAL_PORT_STATUS,
    MESSAGE_TYPE_SWITCH_VLAN_STATUS,
    MESSAGE_TYPE_UNICAST_CLOCKING_STATUS,
    MESSAGE_TYPE_UPGRADE_STATUS,
    MESSAGE_TYPE_VERSIONS_STATUS,
]

MESSAGE_TYPE_CONTROL = [
    MESSAGE_TYPE_ACCESS_CONTROL,
    MESSAGE_TYPE_AES67_CONTROL,
    MESSAGE_TYPE_CLEAR_CONFIG_CONTROL,
    MESSAGE_TYPE_CLOCKING_CONTROL,
    MESSAGE_TYPE_CODEC_CONTROL,
    MESSAGE_TYPE_CONFIG_CONTROL,
    MESSAGE_TYPE_DDM_ENROLMENT_CONFIG_CONTROL,
    MESSAGE_TYPE_EDK_BOARD_CONTROL,
    MESSAGE_TYPE_ENCODING_CONTROL,
    MESSAGE_TYPE_HAREMOTE_CONTROL,
    MESSAGE_TYPE_IGMP_VERS_CONTROL,
    MESSAGE_TYPE_INTERFACE_CONTROL,
    MESSAGE_TYPE_METERING_CONTROL,
    MESSAGE_TYPE_NAME_ID_CONTROL,
    MESSAGE_TYPE_RX_ERROR_THRESHOLD_CONTROL,
    MESSAGE_TYPE_SAMPLE_RATE_CONTROL,
    MESSAGE_TYPE_SAMPLE_RATE_PULLUP_CONTROL,
    MESSAGE_TYPE_SERIAL_PORT_CONTROL,
    MESSAGE_TYPE_SWITCH_VLAN_CONTROL,
    MESSAGE_TYPE_UNICAST_CLOCKING_CONTROL,
    MESSAGE_TYPE_UPGRADE_CONTROL,
]

MESSAGE_TYPE_QUERY = [
    MESSAGE_TYPE_AUDIO_INTERFACE_QUERY,
    MESSAGE_TYPE_IDENTIFY_QUERY,
    MESSAGE_TYPE_IFSTATS_QUERY,
    MESSAGE_TYPE_LED_QUERY,
    MESSAGE_TYPE_LOCK_QUERY,
    MESSAGE_TYPE_MANF_VERSIONS_QUERY,
    MESSAGE_TYPE_MASTER_QUERY,
    MESSAGE_TYPE_RX_CHANNEL_RX_ERROR_QUERY,
    MESSAGE_TYPE_VERSIONS_QUERY,
]

MESSAGE_TYPE_CHANGE = [
    MESSAGE_TYPE_PROPERTY_CHANGE,
    MESSAGE_TYPE_ROUTING_DEVICE_CHANGE,
    MESSAGE_TYPE_RX_CHANNEL_CHANGE,
    MESSAGE_TYPE_RX_FLOW_CHANGE,
    MESSAGE_TYPE_TOPOLOGY_CHANGE,
    MESSAGE_TYPE_TX_CHANNEL_CHANGE,
    MESSAGE_TYPE_TX_FLOW_CHANGE,
    MESSAGE_TYPE_TX_LABEL_CHANGE,
]

MESSAGE_TYPE_MONITORING_STRINGS = {MESSAGE_TYPE_VOLUME_LEVELS: "Volume Levels"}

MESSAGE_TYPE_STRINGS = {
    MESSAGE_TYPE_ACCESS_CONTROL: "Access Control",
    MESSAGE_TYPE_ACCESS_STATUS: "Access Status",
    MESSAGE_TYPE_AES67_STATUS: "AES67 Status",
    MESSAGE_TYPE_AUDIO_INTERFACE_QUERY: "Audio Interface Query",
    MESSAGE_TYPE_AUDIO_INTERFACE_STATUS: "Audio Interface Status",
    MESSAGE_TYPE_CLEAR_CONFIG_STATUS: "Clear Config Status",
    MESSAGE_TYPE_CLOCKING_CONTROL: "Clocking Control",
    MESSAGE_TYPE_CLOCKING_STATUS: "Clocking Status",
    MESSAGE_TYPE_CODEC_CONTROL: "Codec Control",
    MESSAGE_TYPE_CODEC_STATUS: "Codec Status",
    MESSAGE_TYPE_CONFIG_CONTROL: "Config Control",
    MESSAGE_TYPE_DEVICE_REBOOT: "Device Reboot",
    MESSAGE_TYPE_EDK_BOARD_CONTROL: "EDK Board Control",
    MESSAGE_TYPE_EDK_BOARD_STATUS: "EDK Board Status",
    MESSAGE_TYPE_ENCODING_CONTROL: "Encoding Control",
    MESSAGE_TYPE_ENCODING_STATUS: "Encoding Status",
    MESSAGE_TYPE_IDENTIFY_QUERY: "Identify Query",
    MESSAGE_TYPE_IDENTIFY_STATUS: "Identify Status",
    MESSAGE_TYPE_IFSTATS_QUERY: "Ifstats query",
    MESSAGE_TYPE_IFSTATS_STATUS: "Ifstats status",
    MESSAGE_TYPE_IGMP_VERS_CONTROL: "IGMP Version Control",
    MESSAGE_TYPE_IGMP_VERS_STATUS: "IGMP Version Status",
    MESSAGE_TYPE_INTERFACE_CONTROL: "Interface Control",
    MESSAGE_TYPE_INTERFACE_STATUS: "Interface Status",
    MESSAGE_TYPE_LED_QUERY: "LED Query",
    MESSAGE_TYPE_LED_STATUS: "LED Status",
    MESSAGE_TYPE_LOCK_QUERY: "Lock Query",
    MESSAGE_TYPE_LOCK_STATUS: "Lock Status",
    MESSAGE_TYPE_MASTER_QUERY: "Master Query",
    MESSAGE_TYPE_MASTER_STATUS: "Master Status",
    MESSAGE_TYPE_METERING_CONTROL: "Metering Control",
    MESSAGE_TYPE_METERING_STATUS: "Metering Status",
    MESSAGE_TYPE_NAME_ID_CONTROL: "Name Id Query",
    MESSAGE_TYPE_NAME_ID_STATUS: "Name Id Status",
    MESSAGE_TYPE_PROPERTY_CHANGE: "Property change",
    MESSAGE_TYPE_ROUTING_DEVICE_CHANGE: "Routing Device Change",
    MESSAGE_TYPE_ROUTING_READY: "Routing Ready",
    MESSAGE_TYPE_RX_CHANNEL_CHANGE: "Rx Channel Change",
    MESSAGE_TYPE_RX_CHANNEL_RX_ERROR_QUERY: "Rx Channel Rx Error Control",
    MESSAGE_TYPE_RX_CHANNEL_RX_ERROR_STATUS: "Rx Channel Rx Error Status",
    MESSAGE_TYPE_RX_ERROR_THRESHOLD_CONTROL: "Rx Error Threshold Control",
    MESSAGE_TYPE_RX_ERROR_THRESHOLD_STATUS: "Rx Error Threshold Status",
    MESSAGE_TYPE_RX_FLOW_CHANGE: "Rx Flow Change",
    MESSAGE_TYPE_SAMPLE_RATE_CONTROL: "Sample Rate Control",
    MESSAGE_TYPE_SAMPLE_RATE_PULLUP_CONTROL: "Sample Rate Pullup Control",
    MESSAGE_TYPE_SAMPLE_RATE_PULLUP_STATUS: "Sample Rate Pullup Status",
    MESSAGE_TYPE_SAMPLE_RATE_STATUS: "Sample Rate Status",
    MESSAGE_TYPE_SERIAL_PORT_CONTROL: "Serial Port Control",
    MESSAGE_TYPE_SERIAL_PORT_STATUS: "Serial Port Status",
    MESSAGE_TYPE_SWITCH_VLAN_STATUS: "VLAN Status",
    MESSAGE_TYPE_SYS_RESET: "Sys Reset",
    MESSAGE_TYPE_TOPOLOGY_CHANGE: "Topology Change",
    MESSAGE_TYPE_TX_CHANNEL_CHANGE: "Tx Channel Change",
    MESSAGE_TYPE_TX_FLOW_CHANGE: "Tx Flow Change",
    MESSAGE_TYPE_TX_LABEL_CHANGE: "Tx Label Change",
    MESSAGE_TYPE_UNICAST_CLOCKING_CONTROL: "Unicast Clocking Control",
    MESSAGE_TYPE_UNICAST_CLOCKING_STATUS: "Unicast Clocking Status",
    MESSAGE_TYPE_UPGRADE_CONTROL: "Upgrade Control",
    MESSAGE_TYPE_UPGRADE_STATUS: "Upgrade Status",
    REQUEST_DANTE_MODEL: "Version Query",
    REQUEST_MAKE_MODEL: "Manf Versions Query",
    RESPONSE_DANTE_MODEL: "Versions Status",
    RESPONSE_MAKE_MODEL: "Manf Versions Status",
}

MESSAGE_TYPES = [
    MESSAGE_TYPE_ACCESS_CONTROL,
    MESSAGE_TYPE_ACCESS_STATUS,
    MESSAGE_TYPE_AES67_CONTROL,
    MESSAGE_TYPE_AES67_STATUS,
    MESSAGE_TYPE_AUDIO_INTERFACE_QUERY,
    MESSAGE_TYPE_AUDIO_INTERFACE_STATUS,
    MESSAGE_TYPE_CLEAR_CONFIG_CONTROL,
    MESSAGE_TYPE_CLEAR_CONFIG_STATUS,
    MESSAGE_TYPE_CLOCKING_CONTROL,
    MESSAGE_TYPE_CLOCKING_STATUS,
    MESSAGE_TYPE_CODEC_CONTROL,
    MESSAGE_TYPE_CODEC_STATUS,
    MESSAGE_TYPE_CONFIG_CONTROL,
    MESSAGE_TYPE_DDM_ENROLMENT_CONFIG_CONTROL,
    MESSAGE_TYPE_DDM_ENROLMENT_CONFIG_STATUS,
    MESSAGE_TYPE_DEVICE_REBOOT,
    MESSAGE_TYPE_EDK_BOARD_CONTROL,
    MESSAGE_TYPE_EDK_BOARD_STATUS,
    MESSAGE_TYPE_ENCODING_CONTROL,
    MESSAGE_TYPE_ENCODING_STATUS,
    MESSAGE_TYPE_HAREMOTE_CONTROL,
    MESSAGE_TYPE_HAREMOTE_STATUS,
    MESSAGE_TYPE_IDENTIFY_QUERY,
    MESSAGE_TYPE_IDENTIFY_STATUS,
    MESSAGE_TYPE_IFSTATS_QUERY,
    MESSAGE_TYPE_IFSTATS_STATUS,
    MESSAGE_TYPE_IGMP_VERS_CONTROL,
    MESSAGE_TYPE_IGMP_VERS_STATUS,
    MESSAGE_TYPE_INTERFACE_CONTROL,
    MESSAGE_TYPE_INTERFACE_STATUS,
    MESSAGE_TYPE_LED_QUERY,
    MESSAGE_TYPE_LED_STATUS,
    MESSAGE_TYPE_LOCK_QUERY,
    MESSAGE_TYPE_LOCK_STATUS,
    MESSAGE_TYPE_MANF_VERSIONS_QUERY,
    MESSAGE_TYPE_MANF_VERSIONS_STATUS,
    MESSAGE_TYPE_MASTER_QUERY,
    MESSAGE_TYPE_MASTER_STATUS,
    MESSAGE_TYPE_METERING_CONTROL,
    MESSAGE_TYPE_METERING_STATUS,
    MESSAGE_TYPE_NAME_ID_CONTROL,
    MESSAGE_TYPE_NAME_ID_STATUS,
    MESSAGE_TYPE_PROPERTY_CHANGE,
    MESSAGE_TYPE_ROUTING_DEVICE_CHANGE,
    MESSAGE_TYPE_ROUTING_READY,
    MESSAGE_TYPE_RX_CHANNEL_CHANGE,
    MESSAGE_TYPE_RX_CHANNEL_RX_ERROR_QUERY,
    MESSAGE_TYPE_RX_CHANNEL_RX_ERROR_STATUS,
    MESSAGE_TYPE_RX_ERROR_THRESHOLD_CONTROL,
    MESSAGE_TYPE_RX_ERROR_THRESHOLD_STATUS,
    MESSAGE_TYPE_RX_FLOW_CHANGE,
    MESSAGE_TYPE_SAMPLE_RATE_CONTROL,
    MESSAGE_TYPE_SAMPLE_RATE_PULLUP_CONTROL,
    MESSAGE_TYPE_SAMPLE_RATE_PULLUP_STATUS,
    MESSAGE_TYPE_SAMPLE_RATE_STATUS,
    MESSAGE_TYPE_SERIAL_PORT_CONTROL,
    MESSAGE_TYPE_SERIAL_PORT_STATUS,
    MESSAGE_TYPE_SWITCH_VLAN_CONTROL,
    MESSAGE_TYPE_SWITCH_VLAN_STATUS,
    MESSAGE_TYPE_SYS_RESET,
    MESSAGE_TYPE_TOPOLOGY_CHANGE,
    MESSAGE_TYPE_TX_CHANNEL_CHANGE,
    MESSAGE_TYPE_TX_FLOW_CHANGE,
    MESSAGE_TYPE_TX_LABEL_CHANGE,
    MESSAGE_TYPE_UNICAST_CLOCKING_CONTROL,
    MESSAGE_TYPE_UNICAST_CLOCKING_STATUS,
    MESSAGE_TYPE_UPGRADE_CONTROL,
    MESSAGE_TYPE_UPGRADE_STATUS,
    MESSAGE_TYPE_VERSIONS_QUERY,
    MESSAGE_TYPE_VERSIONS_STATUS,
]
