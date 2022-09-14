from django.contrib import admin

from .models.usuario import Usuario
from .models.especialidad import Especialidad
from .models.familiar import Familiar
from .models.historiaclinica import HistoriaClinica
from .models.paciente import Paciente
from .models.personalsalud import PersonalSalud
from .models.signosvitales import SignosVitales

admin.site.register(Usuario)
admin.site.register(Especialidad)
admin.site.register(Familiar)
admin.site.register(HistoriaClinica)
admin.site.register(Paciente)
admin.site.register(PersonalSalud)
admin.site.register(SignosVitales)

# Register your models here.
