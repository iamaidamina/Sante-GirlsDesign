from dataclasses import fields
from rest_framework import serializers
from authApp.models.personalsalud import PersonalSalud

class PersonalSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonalSalud
        fields=['especialidad_id','User_id','nombre','apellido','tipo_documento','numero_documento','fecha_nacimiento','genero', 'telefono', 'correo_electronico', 'registro'] 

# especialidad_id and User_id are foreign keys