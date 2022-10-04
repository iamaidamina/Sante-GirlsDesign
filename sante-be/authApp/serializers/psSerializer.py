from rest_framework import serializers
from authApp.models.personalsalud import PersonalSalud

class PsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalSalud
        fields = ['ps_id','especialidad_id','User_id','nombre','apellido','tipo_documento','numero_documento','fecha_nacimiento','genero','telefono','correo_electronico','registro']
        def create(self, validated_data):
            psInstance = PersonalSalud.objects.create(**validated_data)
            return psInstance
        def to_representation(self, obj):
            ps = PersonalSalud.objects.get(id=obj.id)
            return {
            'ps_id': ps.ps_id,
            'especialidad_id': ps.especialidad_id,
            'User_id': ps.id,
            'nombre': ps.nombre,
            'apellido': ps.apellido,
            'tipo_documento': ps.tipo_documento,
            'numero_documento': ps.numero_documento,
            'fecha_nacimiento': ps.fecha_nacimiento,
            'genero': ps.genero,
            'telefono': ps.telefono,
            'correo_electronico': ps.correo_electronico,
            'registro': ps.registro,
                    
        }