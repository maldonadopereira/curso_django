# Generated by Django 4.0.6 on 2022-07-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='vimeo_id',
            field=models.CharField(default='1', max_length=32, verbose_name='Vimeo ID'),
        ),
    ]
