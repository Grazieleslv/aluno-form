from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('criar/', views.criar_aluno, name='criar_aluno'),
]