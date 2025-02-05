# Generated by Django 5.1 on 2024-09-02 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('curso', models.CharField(choices=[('informatica', 'Informática'), ('alimentos', 'alimentos'), ('apicultura', 'Apicultura'), ('ads', 'ADS'), ('quimica', 'Química'), ('agroindustria', 'Agroindústria')], max_length=14)),
            ],
        ),
    ]
