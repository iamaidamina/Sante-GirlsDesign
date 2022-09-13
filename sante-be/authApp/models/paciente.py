from django.db import models
from .personalsalud import PersonalSalud
from .usuario import Usuario

class Paciente(models.Model):
    paciente_id = models.AutoField(primary_key=True)
    ps_id = models.ForeignKey(PersonalSalud, related_name='paciente', on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario, related_name='paciente', on_delete=models.CASCADE)
    nombre = models.CharField('nombre',max_length=100)
    apellido = models.CharField('apellido',max_length=100)
    tipo_documento = models.CharField('tipo_documento',max_length=10)
    numero_documento = models.CharField('numero_documento',max_length=100)
    fecha_nacimiento = models.DateField('fecha_nacimiento')
    genero = models.CharField('genero',max_length=20)
    telefono = models.CharField('telefono',max_length=15)
    correo_electronico = models.EmailField('correo_electronico',max_length=100)
    direccion = models.CharField('direccion',max_length=150)
    ciudad = models.CharField('ciudad',max_length=150)
    latitud_longitud = models.CharField('latitud_longitud',max_length=300)

