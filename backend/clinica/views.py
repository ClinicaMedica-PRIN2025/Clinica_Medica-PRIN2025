from rest_framework.viewsets import ModelViewSet
from .models import Medico, Especialidade, Paciente, Atendente
from .serializers import MedicoSerializer, EspecialidadeSerializer, PacienteSerializer, AtendenteSerializer

class EspecialidadeViewSet(ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    
class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class AtendenteViewSet(ModelViewSet):
    queryset = Atendente.objects.all()
    serializer_class = AtendenteSerializer