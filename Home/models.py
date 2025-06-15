from django.db import models

# Create your models here.
class Events(models.Model):
    event = models.CharField(max_length=30)
    date = models.DateField()
    for_class = models.IntegerField(null=True)
    number = models.IntegerField(null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    def __str__(self):
        return self.event
    
class student_data(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=16)
    image = models.ImageField(upload_to='Student_Data/', null= True, blank=True)

    def __str__(self):
        return self.name