# Generated by Django 5.0.6 on 2024-05-30 06:01

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cui', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999)])),
                ('nombre', models.CharField(max_length=100)),
                ('anio', models.SmallIntegerField(choices=[(1, 'Primero'), (2, 'Segundo'), (3, 'Tercero'), (4, 'Cuarto'), (5, 'Quinto')])),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NotasAlumnosPorCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultaNotas.alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultaNotas.curso')),
            ],
        ),
    ]
