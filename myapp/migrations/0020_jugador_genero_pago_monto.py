# Generated by Django 4.0.6 on 2022-08-17 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_remove_pago_monto'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='genero',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='pago',
            name='monto',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
