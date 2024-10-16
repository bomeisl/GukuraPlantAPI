from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Plant
from .serializers import PlantSerializer

@api_view(['GET'])
def plant_list():
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plant(request, name):
    try:
        plant = Plant.objects.get(name=name)
        serializer = PlantSerializer(plant)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)







