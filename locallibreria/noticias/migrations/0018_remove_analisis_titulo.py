# Generated by Django 3.1.2 on 2020-10-31 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0017_analisis_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analisis',
            name='titulo',
        ),
    ]
