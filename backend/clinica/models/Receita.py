from django.db import models
from . import Consulta, Medicamento


class Receita(models.Model):
    inicioDosagem = models.DateField(null=False)
    quantidade = models.IntegerField(null=False)
    consulta = models.ForeignKey(Consulta, on_delete=models.PROTECT)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)

    def __str__(self):
        return f"Receita iniciada em {self.inicioDosagem.strftime('%d/%m/%Y')} com quantidade {self.quantidade}"
