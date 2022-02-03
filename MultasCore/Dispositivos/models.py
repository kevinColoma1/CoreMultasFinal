from django.db import models

# Create your models here.

class Dispositivos(models.Model):
    id = models.AutoField(primary_key = True)
    dispositivo = models.CharField(max_length=25)
    