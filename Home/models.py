from django.db import models
from datetime import date

class Events(models.Model):
    event = models.CharField(max_length=100, verbose_name="Event Title")
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    type = models.CharField(max_length=30,default="Program", verbose_name="Event Type")
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    available = models.IntegerField(null=True, blank=True)
    venue = models.CharField(max_length=100, default='TBD')
    Money = models.IntegerField(null=True, blank=True)
    for_class = models.CharField(max_length=30, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.event} ({self.start_date})"
    
class student(models.Model):
    fullname = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    classess = models.CharField(max_length=30)

    def __str__(self):
        return self.fullname