import logging

HOST = 'localhost'
DEFAULT_PORT = 50000
BUFFER = 1024

logging.basicConfig(
    level=logging.DEBUG,
    datefmt='%y-%m-%d %H:%M:%S',
    format='%(asctime)s (%(threadName)-10s) %(name)s: %(message)s',
)
