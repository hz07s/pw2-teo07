from django.db import models

class Persona(models.Model):
    nombres   = models.TextField(max_length=100)
    apellidos = models.TextField(max_length=100)
    edad      = models.IntegerField(blank=True)
    donador   = models.BooleanField()