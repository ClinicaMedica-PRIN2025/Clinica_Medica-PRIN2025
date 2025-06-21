from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet, EspecialidadeViewSet

router = DefaultRouter()
router.register(r'Medico', MedicoViewSet)
router.register(r'Especialidade', EspecialidadeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]