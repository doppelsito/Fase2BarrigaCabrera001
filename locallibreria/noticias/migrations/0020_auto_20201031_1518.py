# Generated by Django 3.1.2 on 2020-10-31 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0019_auto_20201031_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analisis',
            name='puntuacion',
            field=models.DecimalField(decimal_places=1, max_digits=1),
        ),
    ]