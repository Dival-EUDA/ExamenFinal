from django.db import models

# Create your models here.

class Examen(models.Model):
    pk_examen = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    curso = models.CharField(max_length=50, blank=False, null=False)
    punteo = models.CharField(max_length=50, blank=False, null=False)
    bimestre = models.CharField(max_length=50, blank=False, null=False)
    punteo = models.CharField(max_length=100, blank=False, null=True)
    descripcion = models.TextField(blank=False, null=True)