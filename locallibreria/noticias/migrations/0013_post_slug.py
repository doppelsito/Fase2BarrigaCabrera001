# Generated by Django 3.1.2 on 2020-10-31 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0012_remove_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]