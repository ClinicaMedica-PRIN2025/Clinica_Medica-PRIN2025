from django.contrib import admin
from .models import Medico, Especialidade


admin.site.register(Medico, Especialidade)