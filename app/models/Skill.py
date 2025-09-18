from django.db import models
from .User import User


class Skill(models.Model):
    SKILL_TYPE_CHOICES = [
        ("TECH", "Técnica"),
        ("SOFT", "Blanda"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=1, verbose_name="Nivel (1-10)")
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="category",
    )
    skill_type = models.CharField(
        max_length=4,
        choices=SKILL_TYPE_CHOICES,
        default="TECH",
        verbose_name="Tipo de habilidad",
    )
    certification = models.CharField(max_length=100, blank=True, null=True)
    example = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_skill_type_display()})"

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
