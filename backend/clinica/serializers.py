from rest_framework.serializers import ModelSerializer
from .models import Medico, Especialidade, Paciente, Atendente

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