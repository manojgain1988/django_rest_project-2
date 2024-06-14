from rest_framework import serializers
from ProjectApp.models import Industry, Company, Person


class IndustrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Industry
        fields = ('id','url','name','code')


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id','url','name','industry')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id','url','name','companies')
