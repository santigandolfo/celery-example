from logging import getLogger

from celery import Celery

from domain.settings import BROKER
from domain.usecases import add

LOGGER = getLogger(__name__)

app = Celery(__name__, broker=BROKER)


@app.task(acks_late=True)
def add_task(x: int, y: int) -> None:
    LOGGER.info('Starting add task')
    add(1, 2)
    LOGGER.info('Finished add task')
