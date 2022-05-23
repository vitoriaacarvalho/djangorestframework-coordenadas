from ctypes import POINTER
from rest_framework import serializers
from .models import *

class pointSerializer(serializers.ModelSerializer):
    class Meta:
        model = point
        fields = "__all__"
        read_only_fields = ("id",)
        
class lineSerializer(serializers.ModelSerializer):
    class Meta:
        model = line
        fields = "__all__"
        read_only_fields = ("id",)

class polygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = polygon
        fields = "__all__"
        read_only_fields = ("id",)

class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Image
        fields="__all__"
        read_only_fields=("id",)