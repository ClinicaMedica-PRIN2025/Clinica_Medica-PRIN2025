# from django.db import models

# class Especialidade(models.Model):
#     nome = models.CharField(max_length=80, unique=True, null=False)
#     descricao = models.TextField(null=True)

#     def __str__(self):
#         return f"{self.nome}"

# class Medico(models.Model):
#     especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT, null=True)
#     nome = models.CharField(max_length=80, null=False)
#     cpf = models.CharField(max_length=14, unique=True, null=False)
#     cim = models.CharField(max_length=10, unique=True, null=False)
#     email = models.EmailField(max_length=80, unique=True, null=False)
#     telefone = models.CharField(max_length=19, unique=True, null=False)
#     nascimento = models.DateField(null=False)
#     entrada = models.DateField(null=False)

#     def __str__(self):
#         return f"{self.nome}"

# class Paciente(models.Model):
#     nome = models.CharField(max_length=80, null=False)
#     cpf = models.CharField(max_length=14, unique=True, null=False)
#     email = models.EmailField(max_length=80, unique=True, null=False)
#     telefone = models.CharField(max_length=19, unique=True, null=False)
#     nascimento = models.DateField(null=False)

#     def __str__(self):
#         return f"{self.nome}"
    
# class Atendente(models.Model):
#     nome = models.CharField(max_length=80, null=False)
#     cpf = models.CharField(max_length=14, unique=True, null=False)
#     email = models.EmailField(max_length=80, unique=True, null=False)
#     telefone = models.CharField(max_length=19, unique=True, null=False)
#     nascimento = models.DateField(null=False)

#     def __str__(self):
#         return f"{self.nome}"

# class Sala(models.Model):
#     nome_sala = models.CharField(max_length=40)

#     def __str__(self):
#         return f'Sala {self.nome_sala}'
    
# class Consulta(models.Model):
#     atendente = models.ForeignKey(Atendente, on_delete=models.PROTECT, null=True)
#     medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
#     paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
#     data = models.DateTimeField(null=False)
#     sala = models.ForeignKey(Sala, on_delete=models.PROTECT)

#     def __str__(self):
#         return f"Consulta de {self.paciente.nome} com {self.medico.nome}, na sala {self.sala} em {self.data.strftime('%d/%m/%Y %H:%M')}"

# class Exame(models.Model):
#     medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
#     consulta = models.ForeignKey(Consulta, on_delete=models.PROTECT)
#     data = models.DateTimeField(null=False)
#     sala = models.ForeignKey(Sala, on_delete=models.PROTECT)

#     def __str__(self):
#         return f"Exame de {self.consulta.paciente.nome} na sala {self.sala} em {self.data.strftime('%d/%m/%Y %H:%M')}"

# class Fornecedor(models.Model):
#     nome = models.CharField(max_length=80, null=False)
#     cpf = models.CharField(max_length=14, unique=True, null=True)
#     email = models.EmailField(max_length=80, unique=True, null=False)
#     telefone = models.CharField(max_length=19, unique=True, null=False)

#     def __str__(self):
#         return f"{self.nome}"
   
# class Medicamento(models.Model):
#     nome = models.CharField(max_length=80, null=False)
#     descricao = models.TextField(null=True, blank=True)
#     faixaEtaria = models.IntegerField(null=False)
#     dosagem = models.CharField(max_length=45, null=False)
#     fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, null=True)
#     intervalos = models.IntegerField(null=False)

#     def __str__(self):
#         return f"{self.nome} - {self.descricao if self.descricao else 'Sem descrição'}"

# class Receita(models.Model):
#     inicioDosagem = models.DateField(null=False)
#     quantidade = models.IntegerField(null=False)
#     consulta = models.ForeignKey(Consulta, on_delete=models.PROTECT)
#     medicamento = models.ForeignKey(Medicamento, on_delete=models.PROTECT)

#     def __str__(self):
#         return f"Receita iniciada em {self.inicioDosagem.strftime('%d/%m/%Y')} com quantidade {self.quantidade}"