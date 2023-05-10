# Generated by Django 4.1.7 on 2023-05-05 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('nome', models.CharField(max_length=50)),
                ('data_nasc', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=11)),
                ('cnh', models.CharField(max_length=11)),
                ('endereco', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=30)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=10)),
            ],
        ),
    ]
