from django.db import models


# Create your models here.
class Picture(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    publish_date = models.DateField()

    def __str__(self):
        return self.title
