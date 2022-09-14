# Generated by Django 4.0.6 on 2022-08-17 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_horario_partido_primer_equipo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario_partido',
            name='jugador',
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anotaciones', models.IntegerField()),
                ('faltas', models.IntegerField()),
                ('asistencias', models.BooleanField()),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.jugador')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.horario_partido')),
            ],
        ),
    ]
