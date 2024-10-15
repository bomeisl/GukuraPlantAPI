from django.db import models
from django.db.models import TextField
from rest_framework.fields import IntegerField


class Plant(models.Model):
    name = models.TextField()
    upperTemperature = models.IntegerField()
    lowerTemperature = models.IntegerField()
    upperHumidity = models.IntegerField()
    lowerHumidity = models.IntegerField()
    upperLight = models.TextField()
    lowerLight = models.TextField()
