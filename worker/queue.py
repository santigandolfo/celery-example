from logging import getLogger

from celery import Celery

from commons.settings import REDIS
from commons.usecases import add

LOGGER = getLogger(__name__)

redis = REDIS()
redis_url = f'redis://{redis.HOST}:{redis.PORT}/0'

app = Celery(__name__, broker=redis_url)


@app.task(acks_late=True)
def add_task(x: int, y: int) -> None:
    LOGGER.info('Starting add')
    add(1, 2)
    LOGGER.info('Finished add')
