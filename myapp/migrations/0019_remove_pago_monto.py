# Generated by Django 4.0.4 on 2022-08-11 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_remove_jugador_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pago',
            name='monto',
        ),
    ]
