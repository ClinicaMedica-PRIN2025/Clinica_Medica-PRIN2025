from django.db import models


class Sala(models.Model):
    nome_sala = models.CharField(max_length=40)

    def __str__(self):
        return f"Sala {self.nome_sala}"
