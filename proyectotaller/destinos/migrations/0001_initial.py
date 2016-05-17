# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-17 05:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('e_mail', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_categoria', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_Visit', models.TextField(max_length=30)),
                ('foto_Visit', models.FileField(upload_to='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('descripcion', models.TextField(max_length=30)),
                ('spam', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('foto', models.FileField(upload_to='')),
                ('descripcion', models.TextField(max_length=60)),
                ('calificacion', models.FloatField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=20)),
                ('referencia', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=30)),
                ('RUC', models.IntegerField(max_length=10)),
                ('e_mail', models.EmailField(max_length=30)),
                ('telefono', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Extras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=20)),
                ('descripcion', models.TextField(max_length=40)),
                ('telefono', models.CharField(max_length=12)),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos.Distrito')),
            ],
        ),
        migrations.CreateModel(
            name='Privado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=20)),
                ('referencia', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='distrito',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos.Provincia'),
        ),
        migrations.AddField(
            model_name='destino',
            name='distrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos.Distrito'),
        ),
        migrations.AddField(
            model_name='destino',
            name='privado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos.Privado'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos.Destino'),
        ),
    ]