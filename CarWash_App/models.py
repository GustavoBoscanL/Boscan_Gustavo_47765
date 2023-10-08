from django.contrib.auth.models import AbstractUser, User, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_permissions')

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    turno = models.CharField(max_length=10)

class Precio(models.Model):
    tipo_auto = models.CharField(max_length=50)
    lavado_rapido = models.DecimalField(max_digits=5, decimal_places=2)
    lavado_intenso = models.DecimalField(max_digits=5, decimal_places=2)

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
    experiencia = models.TextField()    