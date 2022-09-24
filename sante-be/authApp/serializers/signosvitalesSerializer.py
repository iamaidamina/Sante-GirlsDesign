from dataclasses import fields
from rest_framework import serializers
from authApp.models.signosvitales import SignosVitales

class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=SignosVitales
        fields=['historiaclinica_id','oximetria','frecuencia_respiratoria','frecuencia_cardiaca','temperatura','presion_arterial','glicemia'] 

#historiaclinica_id is foreing key