import requests
from celery import shared_task
from .models import ETLJob, ETLJobRun
from django.utils import timezone
from .transformer import transform_data


@shared_task
def run_etl_job(job_id):
    job = ETLJob.objects.get(id=job_id)
    run = ETLJobRun.objects.create(job=job, status='running', log='Starting ETL job...\n')

    try:
        if job.source_type == 'api':
            url = job.source_config.get('url')
            response = requests.get(url)
            data = response.json()
            run.log += f"Fetched {len(data)} records from {url}\n" # type: ignore

            transformed = transform_data(data)
            run.result = transformed # type: ignore
        else:
            run.log += "Unsupported source type\n" # type: ignore

        run.status = 'success'
        job.status = 'success'
        job.last_run = timezone.now()
        job.save()
        run.log += "Job.finished successfully.\n" # type: ignore

    except Exception as e:
        run.status = 'failed'
        job.status = 'failed'
        run.log += f"Error: {str(e)}\n" # type: ignore

    run.finished_at = timezone.now()
    run.save()
