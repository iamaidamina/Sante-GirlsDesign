from django.db import models
from .historiaclinica import HistoriaClinica

class SignosVitales(models.Model):
    codigo_sv = models.AutoField(primary_key=True)
    historiaclinica_id = models.ForeignKey(HistoriaClinica, related_name='signosvitales', on_delete=models.CASCADE)
    oximetria = models.CharField('oximetria',max_length=25)
    frecuencia_respiratoria = models.CharField('frecuencia_respiratoria',max_length=25)
    frecuencia_cardiaca = models.CharField('frecuencia_cardiaca',max_length=25)
    temperatura = models.CharField('temperatura',max_length=25)
    presion_arterial = models.CharField('presion_arterial',max_length=25)
    glicemia = models.CharField('glicemia',max_length=25) 