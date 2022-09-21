from dataclasses import fields
from rest_framework import serializers
from authApp.models.especialidad import Especialidad

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model= Especialidad
        fields=['especialidad_name']

#fields: not include autoincremented fields in models