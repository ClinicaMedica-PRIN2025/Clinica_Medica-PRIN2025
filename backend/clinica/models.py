from django.db import models

class Especialidade(models.Model):
    nome = models.CharField(max_length=80, unique=True, null=False)
    descricao = models.TextField(null=True)

    def __str__(self):
        return f"{self.nome}"

class Medico(models.Model):
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT, null=True)
    nome = models.CharField(max_length=80, null=False)
    cpf = models.CharField(max_length=14, unique=True, null=False)
    cim = models.CharField(max_length=10, unique=True, null=False)
    email = models.EmailField(max_length=80, unique=True, null=False)
    telefone = models.CharField(max_length=19, unique=True, null=False)
    nascimento = models.DateField(null=False)
    entrada = models.DateField(null=False)

    def __str__(self):
        return f"{self.nome}"

class Paciente(models.Model):
    nome = models.CharField(max_length=80, null=False)
    cpf = models.CharField(max_length=14, unique=True, null=False)
    email = models.EmailField(max_length=80, unique=True, null=False)
    telefone = models.CharField(max_length=19, unique=True, null=False)
    nascimento = models.DateField(null=False)

    def __str__(self):
        return f"{self.nome}"
    
class Atendente(models.Model):
    nome = models.CharField(max_length=80, null=False)
    cpf = models.CharField(max_length=14, unique=True, null=False)
    email = models.EmailField(max_length=80, unique=True, null=False)
    telefone = models.CharField(max_length=19, unique=True, null=False)
    nascimento = models.DateField(null=False)

    def __str__(self):
        return f"{self.nome}"

class Sala(models.Model):
    nome_sala = models.CharField(max_length=40)

    def __str__(self):
        return f'Sala {self.nome_sala}'
