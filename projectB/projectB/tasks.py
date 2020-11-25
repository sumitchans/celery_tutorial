from .celery_app import app


@app.task(name="tutorial.task.data_queue_processor",
          queue="data_queue",
          exchange="celery")
def data_queue_processor(num):
    raise NotImplementedError()
