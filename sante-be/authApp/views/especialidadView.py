from authApp.models import Especialidad
from authApp.serializers import EspecialidadSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EspecialidadList(APIView):
    """
    List all especialidades, or create a new especialidad.
    """
    def get(self, request, format=None):
        especialidades = Especialidad.objects.all()
        serializer = EspecialidadSerializer(especialidades, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EspecialidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EspecialidadDetail(APIView):
    """
    Retrieve, update or delete a especialidad instance.
    """
    def get_object(self, pk):
        try:
            return Especialidad.objects.get(pk=pk)
        except Especialidad.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        especialidad = self.get_object(pk)
        serializer = EspecialidadSerializer(especialidad)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        especialidad = self.get_object(pk)
        serializer = EspecialidadSerializer(especialidad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("message: Success")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        especialidad = self.get_object(pk)
        especialidad.delete()
        return Response("message: Success")