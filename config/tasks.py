from celery import shared_task

@shared_task
def print_text():
    print("ETL job executed")
