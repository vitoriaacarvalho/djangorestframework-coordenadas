from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class lineViewSet(viewsets.ModelViewSet):
    queryset = line.objects.all()
    serializer_class = lineSerializer

class pointViewSet(viewsets.ModelViewSet):
    queryset = point.objects.all()
    serializer_class = pointSerializer

class polygonViewSet(viewsets.ModelViewSet):
    queryset = polygon.objects.all()
    serializer_class = polygonSerializer


class imageViewSet(viewsets.ModelViewSet):
    queryset=Image.objects.all()
    serializer_class= imageSerializer



