from django.db import models
from datetime import date

class Events(models.Model):
    event = models.CharField(max_length=100, verbose_name="Event Title")
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    type = models.CharField(max_length=30, default="Program", verbose_name="Event Type")
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    available = models.IntegerField(null=True, blank=True)
    venue = models.CharField(max_length=100, default='TBD')
    Money = models.IntegerField(null=True, blank=True)
    for_class = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.event} ({self.start_date})"


class Student(models.Model):
    first_name = models.CharField(max_length=30, default="Unnamed")
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, default="Unknown")
    dob = models.DateField(default=date.today)
    student_id = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=70, default="changeme123")

    # Address
    street = models.CharField(max_length=70, default="Unknown Street")
    city = models.CharField(max_length=60, default="Kathmandu")
    province = models.CharField(max_length=30, default="Bagmati")
    district = models.CharField(max_length=30, default="Kathmandu")
    zip = models.IntegerField(null=True, blank=True)

    # Contact
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    # Academic
    class_level = models.IntegerField(null=True, blank=True)
    faculty = models.CharField(max_length=40, null=True, blank=True)

    # Other
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"