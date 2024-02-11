# Generated by Django 5.0.2 on 2024-02-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='times',
        ),
        migrations.AddField(
            model_name='partida',
            name='times',
            field=models.ManyToManyField(related_name='partidas', to='players.time'),
        ),
    ]