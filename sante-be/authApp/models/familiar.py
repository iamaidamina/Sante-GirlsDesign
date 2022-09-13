from django.db import models
from .paciente import Paciente
from .usuario import Usuario

class Familiar(models.Model):
    familiar_id = models.AutoField(primary_key=True)
    paciente_id = models.ForeignKey(Paciente, related_name='familiar', on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario, related_name='familiar', on_delete=models.CASCADE)
    nombre = models.CharField('nombre',max_length=100)
    apellido = models.CharField('apellido',max_length=100)
    tipo_documento = models.CharField('tipo_documento',max_length=10)
    numero_documento = models.CharField('numero_documento',max_length=100)
    parentesco = models.CharField('parentesco', max_length=50)
    genero = models.CharField('genero',max_length=20)
    telefono = models.CharField('telefono',max_length=15)
    correo_electronico = models.EmailField('correo_electronico',max_length=100)
  