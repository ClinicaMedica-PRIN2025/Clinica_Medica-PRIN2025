from django.contrib import admin
from .models import Medico, Especialidade, Paciente, Atendente, Sala, Consulta, Exame


admin.site.register(Medico, Especialidade, Paciente, Atendente, Sala, Consulta, Exame)