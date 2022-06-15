import time
from logging import getLogger

LOGGER = getLogger(__name__)


def add(x, y):
    LOGGER.info(f'Adding {x} + {y}')
    time.sleep(4)
    return x + y
