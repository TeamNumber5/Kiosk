from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    JOB_TITLES = (
            ('E','Employee'),
            ('M','Manager'),
            )
    job_title = models.CharField(max_length=9, choices=JOB_TITLES)

