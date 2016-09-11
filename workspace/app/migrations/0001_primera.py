# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-19 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_de_mascota', models.CharField(max_length=35)),
                ('peso', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
                ('tipo_sangre', models.CharField(max_length=20)),
                ('nombre_contacto', models.CharField(max_length=75)),
                ('numero_contatcto', models.CharField(max_length=15)),
                ('nombre_veterinario', models.CharField(max_length=100)),
            ],
        ),
    ]