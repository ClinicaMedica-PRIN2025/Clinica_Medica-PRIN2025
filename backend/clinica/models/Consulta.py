from django.db import models
from . import Atendente, Medico, Paciente, Sala


class Consulta(models.Model):
    atendente = models.ForeignKey(Atendente, on_delete=models.PROTECT, null=True)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    data = models.DateTimeField(null=False)
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)

    def __str__(self):
        return f"Consulta de {self.paciente.nome} com {self.medico.nome}, na sala {self.sala} em {self.data.strftime('%d/%m/%Y %H:%M')}"
