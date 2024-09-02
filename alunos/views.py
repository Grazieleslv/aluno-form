from django.shortcuts import render, redirect

from alunos.forms import FormularioAluno
from .models import Aluno

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})

def criar_aluno(request):
    if request.method == 'POST':
        form = FormularioAluno(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = FormularioAluno()
    return render(request, 'alunos/criar_aluno.html', {'form': form})