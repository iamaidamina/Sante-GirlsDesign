from dataclasses import fields
from rest_framework import serializers
from authApp.models.historiaclinica import HistoriaClinica

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model= HistoriaClinica
        fields=['paciente_id','ps_id', 'diagnostico','evolucion', 'sugerencias_cuidado'] 

#paciente_id and ps_id are foreing keys