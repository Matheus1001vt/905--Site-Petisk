# Generated by Django 2.2.4 on 2019-08-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_ong_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='ong',
            name='telefone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Telefone'),
        ),
    ]
