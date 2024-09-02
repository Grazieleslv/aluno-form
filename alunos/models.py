from django.db import models

OPCOES_CURSOS = [
    ('informatica', 'Informática'),
    ('alimentos', 'alimentos'),
    ('apicultura', 'Apicultura'),
    ('ads', 'ADS'),
    ('quimica', 'Química'),
    ('agroindustria', 'Agroindústria'),
]

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=150)
    cidade = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    curso = models.CharField(choices=OPCOES_CURSOS, max_length=14)

    def __str__(self):
        return self.nome