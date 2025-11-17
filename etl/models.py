from django.db import models


class ETLJob(models.Model):
    SOURCE_TYPES = (
        ("api", "API"),
        ("database", "Database"),
        ("file", "File")
    )

    STATUSES = (
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('success', 'Success'),
        ('failed', 'Failed')
    )

    name = models.CharField(max_length=100)
    source_type = models.CharField(max_length=10, choices=SOURCE_TYPES)
    source_config = models.JSONField(default=dict, blank=True)
    status = models.CharField(max_length=10, choices=STATUSES,
                              default='pending')
    last_run = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.status})"


class ETLJobRun(models.Model):
    job = models.ForeignKey(ETLJob, on_delete=models.CASCADE,
                            related_name='runs')
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=ETLJob.STATUSES,
                              default='pending')
    log = models.TextField(blank=True, null=True)
    result = models.JSONField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Run of {self.job.name} at {self.started_at}"
