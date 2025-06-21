from rest_framework.viewsets import ModelViewSet
from .models import Medico, Especialidade, Paciente
from .serializers import MedicoSerializer, EspecialidadeSerializer, PacienteSerializer

class EspecialidadeViewSet(ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    
class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer