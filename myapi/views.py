from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import CatSerializer
from .serializers import ServiceSerializer
from .models import Cat
from .models import Service

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all().order_by('name')
    serializer_class = CatSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer