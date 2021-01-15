from django.forms import forms, ModelForm
from pyexpat import model

from quizz.quiz_app.models import Aluno


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email']