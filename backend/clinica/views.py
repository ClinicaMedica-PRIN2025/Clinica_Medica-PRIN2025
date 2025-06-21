from rest_framework.viewsets import ModelViewSet
from .models import Medico, Especialidade, Paciente, Atendente, Sala, Consulta, Exame
from .serializers import MedicoSerializer, EspecialidadeSerializer, PacienteSerializer, AtendenteSerializer, SalaSerializer, ConsultaSerializer, ExameSerializer

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

class SalaViewSet(ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class ExameViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ExameSerializer