from django.contrib import admin
from django.db import models

from quizz.quiz_app.models import Pergunta, Aluno, Resposta


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['id', 'enunciado', 'disponivel']

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'criacao']

@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ['pergunta', 'aluno', 'pontos', 'criacao']