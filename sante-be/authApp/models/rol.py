from django.db import models
from .rol import Rol
# date type: DateFile -- EmailFile
#if primary key is not serial or autoincrement (primary_key=True, unique=True, max_length=size)
class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    rol_name = models.CharField('rol',max_length=100)