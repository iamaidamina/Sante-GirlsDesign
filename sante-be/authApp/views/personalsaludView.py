from authApp.models import PersonalSalud
from authApp.serializers import PersonalSaludSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PersonalSaludList(APIView):
    """
    List all personalsalud, or create a new personalsalud.
    """
    def get(self, request, format=None):
        personal = PersonalSalud.objects.all()
        serializer = PersonalSaludSerializer(personal, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonalSaludSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonalSaludDetail(APIView):
    """
    Retrieve, update or delete a personalsalud instance.
    """
    def get_object(self, pk):
        try:
            return PersonalSalud.objects.get(pk=pk)
        except PersonalSalud.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        personal = self.get_object(pk)
        serializer = PersonalSaludSerializer(personal)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        personal = self.get_object(pk)
        serializer = PersonalSaludSerializer(personal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("message: Success")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        personal = self.get_object(pk)
        personal.delete()
        return Response("message: Success")
