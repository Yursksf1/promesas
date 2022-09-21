# Generated by Django 4.0.6 on 2022-08-07 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_jugador_options_alter_subscripcion_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenamientos_jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugador', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('Cantidad_partidos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.horario_partido')),
            ],
        ),
    ]