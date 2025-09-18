from django.db import models
from .User import User

class Category(models.Model):
    name=models.CharField(max_length=250,verbose_name='Nombre')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'