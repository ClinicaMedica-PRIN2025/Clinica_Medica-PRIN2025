from rest_framework.viewsets import ModelViewSet
from .models import Medico, Especialidade, Paciente, Atendente, Sala, Consulta, Exame, Fornecedor, Medicamento
from .serializers import MedicoSerializer, EspecialidadeSerializer, PacienteSerializer, AtendenteSerializer, SalaSerializer, ConsultaSerializer, ExameSerializer, FornecedorSerializer, MedicamentoSerializer

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
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer

class FornecedorViewSet(ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class MedicamentoViewSet(ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer