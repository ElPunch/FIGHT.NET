from django.db import models

# Create your models here.
class Eventos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    localizacion = models.CharField(max_length=100)
    organizador = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=50)
    usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    data = models.DateTimeField()


    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    disciplina = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'