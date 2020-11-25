from .celery import app

from .asynct_task import process_data


@app.task(name="projectA.task.data_queue_processor", queue="data_queue")
def data_queue_processor(num):
    process_data(num)
