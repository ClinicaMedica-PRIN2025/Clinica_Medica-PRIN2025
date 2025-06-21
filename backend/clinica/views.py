from rest_framework.viewsets import ModelViewSet
from .models import Medico, Especialidade
from .serializers import MedicoSerializer, EspecialidadeSerializer

class EspecialidadeViewSet(ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    
class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


