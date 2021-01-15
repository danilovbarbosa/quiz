from django.db import models

class Pergunta(models.Model):
    enunciado = models.TextField()
    alternativas = models.JSONField()
    disponivel = models.BooleanField()
    alternativa_correta = models.IntegerField(
        choices=[
            (0, 'A'),
            (1, 'B'),
            (2, 'C'),
            (3, 'D'),
        ],
    )

class Aluno(models.Model):
    nome = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    criacao = models.DateTimeField(auto_now_add=True)