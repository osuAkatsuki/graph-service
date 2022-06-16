import sys
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

SOCKET_FILE = config("SOCKET_FILE", default="/tmp/graph_service.sock")

MYSQL_DSN = config("MYSQL_DSN", cast=Secret)
REDIS_DSN = config("REDIS_DSN", cast=Secret)

DEBUG = "debug" in map(str.lower, sys.argv)
VERSION = "1.0.0"
