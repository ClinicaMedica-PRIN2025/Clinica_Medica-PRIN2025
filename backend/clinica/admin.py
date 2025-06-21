from django.contrib import admin
from .models import (Medico, Especialidade, Paciente, Atendente, Sala, Consulta, Exame, Fornecedor, Medicamento, Receita)


admin.site.register(Medico)
admin.site.register(Especialidade)
admin.site.register(Paciente)
admin.site.register(Atendente)
admin.site.register(Sala)
admin.site.register(Consulta)
admin.site.register(Exame)
admin.site.register(Fornecedor)
admin.site.register(Medicamento)
admin.site.register(Receita)