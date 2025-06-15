from django.db import models

# Create your models here.
class Events(models.Model):
    event = models.CharField(max_length=30)
    date = models.DateField()
    for_class = models.IntegerField(null=True)
    number = models.IntegerField(null=True)
    description = models.TextField()
    # image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    def __str__(self):
        return self.event