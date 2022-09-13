from django.db import models
from .rol import Rol

class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    rol_id = models.ForeignKey(Rol, related_name='usuario', on_delete=models.CASCADE)
    nombre_usuario = models.CharField('nombre_usuario',max_length=200)
    contrasenha = models.CharField('contrasenha',max_length=20)