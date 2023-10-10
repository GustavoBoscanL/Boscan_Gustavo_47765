from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name='avatar')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Avatar'
        verbose_name_plural = 'Avatars'

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    turno = models.CharField(max_length=10)

class Precio(models.Model):
    tipo_auto = models.CharField(max_length=50, unique=True)
    lavado_simple = models.DecimalField(max_digits=5, decimal_places=2)
    lavado_intenso = models.DecimalField(max_digits=5, decimal_places=2)
    lavado_full = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.tipo_auto

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
    experiencia = models.TextField()    