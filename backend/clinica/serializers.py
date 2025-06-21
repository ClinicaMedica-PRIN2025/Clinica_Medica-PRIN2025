from rest_framework.serializers import ModelSerializer
from .models import Medico, Especialidade, Paciente, Atendente, Sala, Consulta, Exame, Fornecedor, Medicamento, Receita

class EspecialidadeSerializer(ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'

class MedicoSerializer(ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class AtendenteSerializer(ModelSerializer):
    class Meta:
        model = Atendente
        fields = '__all__'

class SalaSerializer(ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

class ConsultaSerializer(ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class ExameSerializer(ModelSerializer):
    class Meta:
        model = Exame
        fields = '__all__'

class FornecedorSerializer(ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class MedicamentoSerializer(ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class ReceitaSerializer(ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'