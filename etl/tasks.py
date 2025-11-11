import requests
from celery import shared_task
from .models import ETLJob
from django.utils import timezone

URL = 'https://jsonplaceholder.typicode.com/todos'

@shared_task
def run_etl_job(job_id):
    job = ETLJob.objects.get(id=job_id)
    job.status = 'running'
    job.save()

    try:
        response = requests.get(URL)
        data = response.json()
        print(f"Fetched {len(data)} records from API.")

        job.status = 'success'
        job.last_run = timezone.now()
        job.save()
    except Exception as e:
        job.status = 'failed'
        job.save()
        print(f"ETL job {job_id} failed {e}")
