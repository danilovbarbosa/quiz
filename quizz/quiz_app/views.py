from django.db.models import Sum
from django.shortcuts import render, redirect
from django.utils.timezone import now

from quizz.quiz_app.forms import AlunoForm
from quizz.quiz_app.models import Pergunta, Aluno, Resposta


def verificar_se_aluno_existe_no_bd(request):
    '''
    Verificar se aluno já existe no BD
    :param request: requisição HTTP
    :return: Aluno
    '''
    email = request.POST['email']
    aluno = Aluno.objects.get(email=email)
    if aluno:
        return aluno

def validar_formulario_aluno(request):
    '''Validar formulário

    :param request:
    :return: redirect('/perguntas/1') or render for index
    '''
    form = AlunoForm(request.POST)
    if form.is_valid():
        # salvar aluno no BD e redirecionar para o quiz
        aluno = form.save()
        request.session['aluno_id'] = aluno.id
        return redirect('/perguntas/1')
    else:
        contexto = {'form': form}
        return render(request, 'quiz_app/index.html', contexto)

def index(request):
    if request.method == 'POST':
        try:
            aluno: Aluno = verificar_se_aluno_existe_no_bd(request)
        except Aluno.DoesNotExist:
            validar_formulario_aluno(request)
        else:
            request.session['aluno_id'] = aluno.id
            return redirect('/perguntas/1')

    return render(request, 'quiz_app/index.html')

def perguntas(request, indice: int):
    aluno_id = request.session['aluno_id']
    try:
        pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]

    except IndexError:
        return redirect('/classificacao')

    else:
        contexto = {
            'indice': indice,
            'pergunta': pergunta,
        }

        if request.method == 'POST':
            alternativa_escolhida = int(request.POST['alternativa'])

            if alternativa_escolhida - 1 == pergunta.alternativa_correta:
                try:
                    primeira_resposta: Resposta = Resposta.objects.filter().order_by('criacao')[0]
                except:
                    pontos = 100
                else:
                    tempo_da_primeira_resposta = primeira_resposta.criacao
                    diferenca = now() - tempo_da_primeira_resposta
                    pontos = 100 - int(diferenca.total_seconds())
                    pontos = max(pontos, 1)

                Resposta(aluno_id = aluno_id, pergunta=pergunta, pontos=pontos).save()

                return redirect(f'/perguntas/{indice + 1}')

            contexto['alternativa_escolhida'] = alternativa_escolhida

        return render(request, 'quiz_app/perguntas.html', contexto)

def classificacao(request):
    aluno_id = request.session['aluno_id']
    pontos_do_aluno = Resposta.objects.filter(aluno_id=aluno_id).aggregate(Sum('pontos'))['pontos__sum']

    aluno_com_pontuacao_maior = Resposta.objects.values('aluno').annotate(Sum('pontos')).filter(
        pontos__sum__gt=pontos_do_aluno).count()

    primeiros_cinco_alunos = Resposta.objects.values('aluno', 'aluno__nome').annotate(Sum('pontos')).filter(
        pontos__sum__gt=pontos_do_aluno).count()

    contexto = {
        'pontos': pontos_do_aluno,
        'posicao': aluno_com_pontuacao_maior + 1,
    }

    return render(request, 'quiz_app/classificacao.html', contexto)

