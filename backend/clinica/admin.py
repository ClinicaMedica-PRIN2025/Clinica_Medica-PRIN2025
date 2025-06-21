from django.contrib import admin
from .models import Medico, Especialidade, Paciente, Atendente


admin.site.register(Medico, Especialidade, Paciente, Atendente)