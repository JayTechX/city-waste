from rest_framework import serializers

from .models import Client,Appointment

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
       #fields =('name','address','price','building')
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
       #fields =('name','address','price','building')
        fields = '__all__'