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
    
class Consulta(models.Model):
    atendente = models.ForeignKey(Atendente, on_delete=models.PROTECT, null=True)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    data = models.DateTimeField(null=False)
    sala = models.ForeignKey(Sala, on_delete=models.PROTECT)

    def __str__(self):
        return f"Consulta de {self.paciente.nome} com {self.medico.nome}, na sala {self.sala} em {self.data.strftime('%d/%m/%Y %H:%M')}"

