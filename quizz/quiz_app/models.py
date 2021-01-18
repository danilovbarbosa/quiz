from django.db import models
from django.db.models import constraints


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

class Resposta(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    pontos = models.IntegerField()
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['aluno', 'pergunta'], name='resposta_unica')
        ]