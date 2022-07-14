from django.db import models

# Create your models here.
from django.db import models
class Clientes(models.Model):
    idCliente = models.CharField(max_length=11, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=20)
    segmento = models.IntegerField()
    nacionalidad = models.CharField(max_length=20)
    rfc = models.CharField(max_length=13,blank=True,null=True)
    tipoID = models.CharField(max_length=50)
    numeroID = models.CharField(max_length=50)
    cuenta = models.CharField(max_length=50)
    email = models.CharField(max_length=50,blank=True,null=True)
    TDD = models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
        return self.idCliente

class Asesores(models.Model):
    usuario = models.CharField(max_length=50)
    auth = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    area = models.CharField(max_length=50)
    segmento = models.IntegerField()
    perfil = models.CharField(max_length=50)
    def __str__(self):
        return self.usuario


