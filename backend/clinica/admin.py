from django.contrib import admin
from .models import Medico, Especialidade, Paciente, Atendente, Sala, Consulta


admin.site.register(Medico, Especialidade, Paciente, Atendente, Sala, Consulta)