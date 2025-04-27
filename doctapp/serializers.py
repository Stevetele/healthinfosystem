from rest_framework import serializers
from .models import Client, HealthProgram

class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = ['id','name']


class ClientSerializer(serializers.ModelSerializer):
    programs = HealthProgramSerializer(many=True)
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'email', 'programs']        