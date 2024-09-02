from django.forms import ModelForm
from .models import Aluno
from django import forms

class FormularioAluno(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'data_nascimento', 'curso', 'cidade', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
        }
