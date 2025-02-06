from django.db import models

class Funcionario(models.Model):
    id = models.CharField(max_length=10, primary_key=True)  # Agora o ID será inserido manualmente
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    rg = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=20, unique=True)
    cnh = models.CharField(max_length=20, blank=True, null=True)
    validade_cnh = models.DateField(blank=True, null=True)
    data_nascimento = models.DateField()
    idade = models.IntegerField()
    contato_pessoal = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')])
    sexo = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')])
    departamento = models.CharField(max_length=50)
    admissao = models.DateField()
    mobilizacao = models.DateField(blank=True, null=True)
    desligamento = models.DateField(blank=True, null=True)
    desmobilizacao = models.DateField(blank=True, null=True)
    cracha_vale_id = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)  # Campo para foto do funcionário

    def __str__(self):
        return self.nome

