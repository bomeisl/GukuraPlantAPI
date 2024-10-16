from django.db import models

from django.core.exceptions import ValidationError
from django.db.models import TextField
from rest_framework.fields import IntegerField

class Plant(models.Model):
    name = models.TextField()
    upper_temperature = models.IntegerField()
    lower_temperature = models.IntegerField()
    upper_humidity = models.IntegerField()
    lower_humidity = models.IntegerField()
    upper_light = models.TextField()
    lower_light = models.TextField()

    class Meta:
        ordering = ['name']

    def clean(self):
        if self.upper_temperature < self.lower_temperature:
            raise ValidationError("Temperature max < min")
        if self.upper_humidity < self.lower_humidity:
            raise ValidationError("Humidity max < min")
        if self.upper_light < self.lower_light:
            raise ValidationError("Light level max < min")
