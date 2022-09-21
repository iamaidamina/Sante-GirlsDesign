from authApp.models import HistoriaClinica
from authApp.serializers import HistoriaClinicaSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HistoriaClinicaList(APIView):
    """
    List all historiasclinicas, or create a new historiaclinica.
    """
    def get(self, request, format=None):
        historiasclinicas = HistoriaClinica.objects.all()
        serializer = HistoriaClinicaSerializer(historiasclinicas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HistoriaClinicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HistoriaClinicaDetail(APIView):
    """
    Retrieve, update or delete a user historiaclinica.
    """
    def get_object(self, pk):
        try:
            return HistoriaClinica.objects.get(pk=pk)
        except HistoriaClinica.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        historiaclinica = self.get_object(pk)
        serializer = HistoriaClinicaSerializer(historiaclinica)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        historiaclinica = self.get_object(pk)
        serializer = HistoriaClinicaSerializer(historiaclinica, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        historiaclinica = self.get_object(pk)
        historiaclinica.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
