from django.shortcuts import render


def index(request):
    return render(request, 'quiz_app/index.html')


def perguntas(request, indice: int):
    return render(request, 'quiz_app/perguntas.html')


def classificacao(request):
    return render(request, 'quiz_app/classificacao.html')

