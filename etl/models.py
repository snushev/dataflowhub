from django.db import models

class ETLJob(models.Model):
    SOURCE_TYPES = (
        ("api","API"),
        ("database","Database"),
        ("file","File")
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
    status =  models.CharField(max_length=10, choices=STATUSES, default='pending')
    last_run = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.status})"
