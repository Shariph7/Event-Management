from django.db import models
from datetime import date

class Events(models.Model):
    event = models.CharField(max_length=30)
    date = models.DateField(default=date.today)
    time = models.TimeField(null=True)
    venue = models.CharField(max_length=30, default='TBD')
    for_class = models.IntegerField(null=True)
    number = models.IntegerField(null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)

    def __str__(self):
        return self.event

class student_data(models.Model):
    student_name = models.CharField(max_length=30)
    date = models.DateField(default=date.today)
    classs = models.IntegerField(null=True)
    image = models.ImageField(upload_to='Student_Data/', null=True, blank=True)

    def __str__(self):
        return self.student_name
