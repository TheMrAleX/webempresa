from django.db import models
import os

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imágen', upload_to='services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado: ')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado: ')

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    