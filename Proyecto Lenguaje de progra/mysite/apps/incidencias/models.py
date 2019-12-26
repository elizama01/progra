from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=10)
    rol = models.CharField(max_length=15)