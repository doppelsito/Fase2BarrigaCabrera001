# Generated by Django 3.1.2 on 2020-11-01 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0027_auto_20201101_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analisis',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='noticias.user'),
        ),
    ]
