from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet, EspecialidadeViewSet, PacienteViewSet, AtendenteViewSet, SalaViewSet

router = DefaultRouter()
router.register(r'Medico', MedicoViewSet)
router.register(r'Especialidade', EspecialidadeViewSet)
router.register(r'Paciente', PacienteViewSet)
router.register(r'Atendente', AtendenteViewSet)
router.register(r'Sala', SalaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]