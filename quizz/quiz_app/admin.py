from django.contrib import admin
from django.db import models

from quizz.quiz_app.models import Pergunta, Aluno


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['id', 'enunciado', 'disponivel']

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'criacao']