from django.contrib.auth.models import Group, User
from rest_framework import serializers
from PlantDB.models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = [
            'name',
            'upper_temperature',
            'lower_temperature',
            'upper_humidity',
            'lower_humidity',
            'upper_light_level',
            'lower_light_level'
        ]

