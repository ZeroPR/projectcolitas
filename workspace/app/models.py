from __future__ import unicode_literals
from django.contrib import admin

from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre_de_mascota = models.CharField(max_length=35)
    peso = models.CharField(max_length=25)
    edad = models.CharField(max_length=20)
    tipo_sangre = models.CharField(max_length=20)
    nombre_contacto = models.CharField(max_length=75)
    numero_contacto = models.CharField(max_length=15)
    nombre_veterinario = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_de_mascota
        
    def __unicode__(self):
        return self.nombre_de_mascota
    

admin.site.register(Mascota)