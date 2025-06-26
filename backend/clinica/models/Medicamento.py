from django.db import models
from . import Fornecedor


class Medicamento(models.Model):
    nome = models.CharField(max_length=80, null=False)
    descricao = models.TextField(null=True, blank=True)
    faixaEtaria = models.IntegerField(null=False)
    dosagem = models.CharField(max_length=45, null=False)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, null=True)
    intervalos = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.nome} - {self.descricao if self.descricao else 'Sem descrição'}"
