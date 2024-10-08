# Generated by Django 4.2.16 on 2024-09-12 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_cedula', models.CharField(max_length=16)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateTimeField(auto_now_add=True)),
                ('telefono', models.CharField(max_length=8)),
                ('correo_electronico', models.CharField(max_length=100, null=True)),
                ('direccion', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
