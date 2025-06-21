from django.contrib import admin
from .models import Medico, Especialidade, Paciente


admin.site.register(Medico, Especialidade, Paciente)