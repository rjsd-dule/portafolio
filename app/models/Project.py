from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os


class Project(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="projects")
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="projects",
    )

    title = models.CharField(max_length=250)
    description = models.TextField()
    url_demo = models.URLField(max_length=250, blank=True, null=True)
    url_repository = models.URLField(max_length=250, blank=True, null=True)
    lenguajes = models.JSONField(default=list, blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)

    def save(self, *args, **kwargs):
        # Si existe un objeto previo (update), verificamos la imagen
        if self.pk:
            old_project = Project.objects.filter(pk=self.pk).first()
            if old_project and old_project.image and self.image != old_project.image:
                old_project.image.delete(save=False)

        # Si hay imagen nueva, renombrarla antes de guardar
        if self.image and hasattr(self.image, "name"):
            print("Si hay imagen nueva")
            ext = os.path.splitext(self.image.name)[1].lower()
            base = os.path.splitext(os.path.basename(self.image.name))[0].lower()
            print(f"Nombre de la imagen {base}")
            self.image.name = f"{base}_{self.user.id}{ext}"
        else:
            print("no hay imagen nueva para actualizar")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Project)
def delete_project_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)
