from authApp.models import Familiar
from authApp.serializers import FamiliarSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FamiliarList(APIView):
    """
    List all familiares, or create a new familiar.
    """
    def get(self, request, format=None):
        familiares = Familiar.objects.all()
        serializer = FamiliarSerializer(familiares, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FamiliarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FamiliarDetail(APIView):
    """
    Retrieve, update or delete a familiar instance.
    """
    def get_object(self, pk):
        try:
            return Familiar.objects.get(pk=pk)
        except Familiar.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        familiar = self.get_object(pk)
        serializer = FamiliarSerializer(familiar)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        familiar = self.get_object(pk)
        serializer = FamiliarSerializer(familiar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("message:Success")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        familiar = self.get_object(pk)
        familiar.delete()
        return Response("message:Success")