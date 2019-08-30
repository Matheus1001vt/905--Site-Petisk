# Generated by Django 2.2.4 on 2019-08-30 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_ong_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('raca', models.CharField(max_length=255, verbose_name='Raça')),
                ('porte', models.CharField(choices=[('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande')], max_length=255, verbose_name='Porte')),
                ('peso', models.FloatField(verbose_name='Peso')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('dono', models.ForeignKey(on_delete=None, to='website.Pessoa')),
            ],
        ),
    ]
