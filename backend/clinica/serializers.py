from rest_framework.serializers import ModelSerializer
from .models import Medico, Especialidade

class EspecialidadeSerializer(ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'

class MedicoSerializer(ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'