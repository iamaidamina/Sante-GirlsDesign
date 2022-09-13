from django.db import models
from .paciente import Paciente
from .personalsalud import PersonalSalud

class HistoriaClinica(models.Model):
    historiaclinica_id = models.AutoField(primary_key=True)
    paciente_id = models.ForeignKey(Paciente, related_name='historiaclinica', on_delete=models.CASCADE)
    ps_id = models.ForeignKey(PersonalSalud, related_name='historiaclinica', on_delete=models.CASCADE)
    diagnostico = models.CharField('diagnostico',max_length=300)
    evolucion = models.CharField('evolucion',max_length=3000)
    sugerencias_cuidado = models.CharField('sugerencias_cuidado',max_length=3000)
  