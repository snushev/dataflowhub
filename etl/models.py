from django.db import models

class ETLJob(models.Model):
    SOURCE_TYPES = (
        ("API","API"),
        ("DB","Database"),
        ("File","File")
    )

    STATUSES = (
        ('pend', 'pending'),
        ('runn', 'running'),
        ('succ', 'success'),
        ('fail', 'failed')
    )

    name = models.CharField(max_length=100)
    source_type = models.CharField(max_length=10, choices=SOURCE_TYPES)
    source_config = models.JSONField()
    status =  models.CharField(max_length=10, choices=STATUSES)
    last_run = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
