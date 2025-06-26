from django.db import models
from . import Medico, Consulta, Sala


class Exame(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    consulta = models.ForeignKey(Consulta, on_delete=models.PROTECT)
    data = models.DateTimeField(null=False)
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)

    def __str__(self):
        return f"Exame de {self.consulta.paciente.nome} na sala {self.sala} em {self.data.strftime('%d/%m/%Y %H:%M')}"
