from authApp.models import Paciente
from authApp.serializers import PacienteSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PacienteList(APIView):
    """
    List all pacientes, or create a new paciente.
    """
    def get(self, request, format=None):
        pacientes = Paciente.objects.all()
        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PacienteDetail(APIView):
    """
    Retrieve, update or delete a paciente instance.
    """
    def get_object(self, pk):
        try:
            return Paciente.objects.get(pk=pk)
        except Paciente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        paciente = self.get_object(pk)
        serializer = PacienteSerializer(paciente)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        paciente = self.get_object(pk)
        serializer = PacienteSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("message: Success")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        paciente = self.get_object(pk)
        paciente.delete()
        return Response("message: Success")