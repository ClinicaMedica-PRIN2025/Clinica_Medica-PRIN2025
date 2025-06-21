from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=80, null=False)
    cpf = models.CharField(max_length=14, unique=True, null=False)
    cim = models.CharField(max_length=10, unique=True, null=False)
    email = models.EmailField(max_length=80, unique=True, null=False)
    telefone = models.CharField(max_length=19, unique=True, null=False)
    nascimento = models.DateField(null=False)
    entrada = models.DateField(null=False)

    def __str__(self):
        return f"{self.nome}"