from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Client,Appointment
from .serializers import ClientSerializer,AppointmentSerializer


#List all clients or create a new one
#client/
class ClientList(APIView):

    def get(self, request):
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)

    def post(self):
        pass

#List all clients or create a new one
#appointment/
class AppointmentList(APIView):

    def get(self, request):
        appointment = Appointment.objects.all()
        serializer =AppointmentSerializer(appointment, many=True)
        return Response(serializer.data)

    def post(self):
        pass