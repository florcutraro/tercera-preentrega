from django.db import models

class Pacientes(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Email = models.EmailField()
    Prepaga = models.CharField(max_length=40)
    Plan = models.CharField(max_length=40)

class Medicos(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Especialidad = models.CharField(max_length=40)

class Otros_Profesionales(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Profesión = models.CharField(max_length=40)
