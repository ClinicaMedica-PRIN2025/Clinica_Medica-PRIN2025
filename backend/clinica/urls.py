from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet, EspecialidadeViewSet, PacienteViewSet, AtendenteViewSet

router = DefaultRouter()
router.register(r'Medico', MedicoViewSet)
router.register(r'Especialidade', EspecialidadeViewSet)
router.register(r'Paciente', PacienteViewSet)
router.register(r'Atendente', AtendenteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]