from django.db import models
from .especialidad import Especialidad
from .usuario import Usuario

class PersonalSalud(models.Model):
    ps_id = models.AutoField(primary_key=True)
    especialidad_id = models.ForeignKey(Especialidad, related_name='personalsalud', on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario, related_name='personalsalud', on_delete=models.CASCADE)
    nombre = models.CharField('nombre',max_length=100)
    apellido = models.CharField('apellido',max_length=100)
    tipo_documento = models.CharField('tipo_documento',max_length=10)
    numero_documento = models.CharField('numero_documento',max_length=100)
    fecha_nacimiento = models.DateField('fecha_nacimiento')
    genero = models.CharField('genero',max_length=20)
    telefono = models.CharField('telefono',max_length=15)
    correo_electronico = models.EmailField('correo_electronico',max_length=100)
    registro = models.CharField('registro',max_length=25)
