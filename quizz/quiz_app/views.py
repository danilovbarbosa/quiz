from django.shortcuts import render

from quizz.quiz_app.models import Pergunta


def index(request):
    return render(request, 'quiz_app/index.html')


def perguntas(request, indice: int):
    pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]

    contexto = {
        'indice': indice,
        'pergunta': pergunta,
    }
    return render(request, 'quiz_app/perguntas.html', contexto)


def classificacao(request):
    return render(request, 'quiz_app/classificacao.html')

