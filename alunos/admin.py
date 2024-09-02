from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'endereco', 'cidade', 'email', 'curso')
