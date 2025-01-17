# server host and port
SERVER_HOST = "localhost"
SERVER_PORT = 6784

# verbosity
VERBOSITY = 1

# Error checking scheme
ERROR_CHECKING = "core.middleware.checks.crc.CRC"

# CRC settings
CRC_KEY = "1001"

# Error generator scheme
ERROR_GENERATOR = "core.device.datalink.error.error_generator"
ERROR_MAX_BITS = 2
ERROR_DISTRIBUTION = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      1, 1, 1, 1, 1, 1, 2, 2, 2, 3]

# Frame Settings
PACKET_SIZE = 32
FRAMING_SCHEME = "core.middleware.framer.bit_stuffing.BitStuffing"
