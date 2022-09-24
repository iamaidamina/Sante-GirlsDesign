from authApp.models import SignosVitales
from authApp.serializers import SignosVitalesSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SignosVitalesList(APIView):
    """
    List all signosvitales, or create a new signosvitales.
    """
    def get(self, request, format=None):
        signosvitales = SignosVitales.objects.all()
        serializer = SignosVitalesSerializer(signosvitales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SignosVitalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignosVitalesDetail(APIView):
    """
    Retrieve, update or delete a signosvitales instance.
    """
    def get_object(self, pk):
        try:
            return SignosVitales.objects.get(pk=pk)
        except SignosVitales.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        signosvitales = self.get_object(pk)
        serializer = SignosVitalesSerializer(signosvitales)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        signosvitales = self.get_object(pk)
        serializer = SignosVitalesSerializer(signosvitales, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("mesagge: Success")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        signosvitales = self.get_object(pk)
        signosvitales.delete()
        return Response("mesagge: Success")
