from django.db import models

class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    rol_name = models.CharField('rol',max_length=100)