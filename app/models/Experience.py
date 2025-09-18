from django.db import models
from .User import User

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=250, verbose_name="Puesto")
    sub_title = models.CharField(max_length=250, verbose_name="Subtítulo Puesto", blank=True, null=True)
    company = models.CharField(max_length=250, verbose_name="Empresa")
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(blank=True, null=True, verbose_name="Fecha de fin")
    description = models.TextField()
    is_current = models.BooleanField(default=False, verbose_name="¿Trabajo actual?")

    def __str__(self):
        return f"{self.job_title} en {self.company}"

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        ordering = ["-start_date"]
