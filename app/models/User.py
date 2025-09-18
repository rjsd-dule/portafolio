from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
import os


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    bio = models.TextField(blank=True, null=True)
    profesion = models.CharField(max_length=200, blank=True)
    profile_document = models.FileField(
        upload_to="profile_docs/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])],
        blank=True,
        null=True,
    )
    profile_picture = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True
    )
    website = models.URLField(max_length=250, blank=True, null=True)
    url_repository = models.URLField(max_length=250, blank=True, null=True)
    url_linkedin = models.URLField(max_length=250, blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombre", "username"]

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_user = User.objects.get(pk=self.pk)
                # --- Imagen ---
                if (
                    old_user.profile_picture
                    and old_user.profile_picture != self.profile_picture
                ):
                    if os.path.isfile(old_user.profile_picture.path):
                        os.remove(old_user.profile_picture.path)

                # --- Documento ---
                if (
                    old_user.profile_document
                    and old_user.profile_document != self.profile_document
                ):
                    if os.path.isfile(old_user.profile_document.path):
                        os.remove(old_user.profile_document.path)
            except User.DoesNotExist:
                pass
        super().save(*args, **kwargs)
