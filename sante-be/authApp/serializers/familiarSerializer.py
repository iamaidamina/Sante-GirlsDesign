from dataclasses import fields
from rest_framework import serializers
from authApp.models.familiar import Familiar

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model= Familiar
        fields=['paciente_id','User_id', 'nombre','apellido', 'tipo_documento','numero_documento','parentesco','genero','telefono','correo_electronico'] 

#paciente_id and User_id are foreing keys
  