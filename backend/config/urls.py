from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from clinica.views import (MedicoViewSet, EspecialidadeViewSet, PacienteViewSet,
                            AtendenteViewSet, SalaViewSet, ConsultaViewSet,
                            ExameViewSet, FornecedorViewSet, MedicamentoViewSet,
                            ReceitaViewSet)

router = DefaultRouter()
router.register(r'medico', MedicoViewSet)
router.register(r'especialidade', EspecialidadeViewSet)
router.register(r'paciente', PacienteViewSet)
router.register(r'atendente', AtendenteViewSet)
router.register(r'sala', SalaViewSet)
router.register(r'consulta', ConsultaViewSet)
router.register(r'exame', ExameViewSet)
router.register(r'fornecedor', FornecedorViewSet)
router.register(r'medicamento', MedicamentoViewSet)
router.register(r'receita', ReceitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]