from django.db import models

class Especialidad(models.Model):
    especialidad_id = models.AutoField(primary_key=True)
    especialidad_name = models.CharField('especialidad',max_length=100)