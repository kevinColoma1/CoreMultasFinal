import imp
from django.db import models
from Dispositivos.models import Dispositivos
from datetime import date
# Create your models here.

class Prestamo(models.Model):
    id = models.AutoField(primary_key=True)
    Fdispositivo = models.ForeignKey(Dispositivos, null = True, blank= True, on_delete=models.CASCADE)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    fechaentrega = models.DateField(null=True)
    Usuario = models.CharField(max_length=25)
    Estado = models.CharField(max_length=25)
    

