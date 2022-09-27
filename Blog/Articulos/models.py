
from django.db import models

# Create your models here.
class Entrada(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cuerpo = models.TextField(max_length=5000)
    autor = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="articulos", null=True)

    def __str__(self):
        return self.titulo