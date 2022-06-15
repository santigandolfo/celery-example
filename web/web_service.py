from logging import getLogger

from fastapi import FastAPI, status
from fastapi import Response

from worker.queue import add_task

LOGGER = getLogger(__name__)

app = FastAPI()


@app.get("/")
def add_endpoint():
    task_id = add_task.delay(x=1, y=2)
    LOGGER.info(f'New add task delayed with id[{task_id}]')

    return Response(content='OK', status_code=status.HTTP_202_ACCEPTED)
