from django.db import models

# Create your models here.
class MiModelo(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    movil = models.IntegerField(null=True)
    fecha_registro = models.DateField(null=True)