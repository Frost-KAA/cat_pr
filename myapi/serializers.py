# serializers.py
from rest_framework import serializers

from .models import Cat
from .models import Service

class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ('id', 'name', 'year', 'desc', 'upload')

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'price')