from django.shortcuts import render
from rest_framework import viewsets, permissions
from ApiApp.serializers import IndustrySerializer,CompanySerializer,PersonSerializer
from .models import Industry,Company,Person
# Create your views here.

class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

