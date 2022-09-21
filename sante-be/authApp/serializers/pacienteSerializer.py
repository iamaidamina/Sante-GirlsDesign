from dataclasses import fields
from rest_framework import serializers
from authApp.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paciente
        fields=['ps_id','User_id','nombre','apellido','tipo_documento','numero_documento','fecha_nacimiento','genero', 'telefono', 'correo_electronico', 'direccion', 'ciudad', 'latitud_longitud'] 

#ps_id  and User_id are foreing keys