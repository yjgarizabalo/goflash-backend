# Generated by Django 4.2.4 on 2023-08-20 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=20, unique=True)),
                ('primer_nombre', models.CharField(max_length=200)),
                ('segundo_nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('primer_apellido', models.CharField(max_length=200)),
                ('segundo_apellido', models.CharField(blank=True, max_length=200, null=True)),
                ('correo', models.EmailField(max_length=100, unique=True)),
                ('correo_personal', models.EmailField(blank=True, max_length=100, null=True)),
                ('usuario', models.CharField(max_length=100, unique=True)),
                ('celular', models.BigIntegerField(null=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_elimino', models.DateTimeField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=10)),
            ],
        ),
    ]