from django.db import models

class Plant(models.Model):
    name = models.TextField()
    upperTemperature = models.IntegerField()
    lowerTemperature = models.IntegerField()
    upperHumidity = models.IntegerField()
    lowerHumidity = models.IntegerField()
    upperLight = models.TextField()
    lowerLight = models.TextField()
