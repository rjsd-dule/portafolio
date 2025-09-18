from django import forms
from app.models import Project
from app.models import Category


class ProjectForm(forms.ModelForm):
    lenguajes = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Category"}
        ),
        help_text="Separa los lenguajes con comas",
    )

    class Meta:
        model = Project
        fields = [
            "category",
            "title",
            "description",
            "url_demo",
            "url_repository",
            "lenguajes",
            "image",
        ]

        widgets = {
            "category": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: Dule_developer"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Describe tu proyecto en detalle...",
                }
            ),
            "url_demo": forms.URLInput(
                attrs={"class": "form-control", "placeholder": "https://tudemo.com"}
            ),
            "url_repository": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://github.com/usuario/repo",
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",  # Solo aceptar imágenes
                }
            ),
        }

        help_texts = {
            "url_demo": "URL donde se puede ver el proyecto en funcionamiento",
            "url_repository": "URL del repositorio (GitHub, GitLab, etc.)",
            "image": "Imagen representativa del proyecto",
        }

        labels = {
            "title": "Título del Proyecto",
            "description": "Descripción",
            "url_demo": "URL de Demo",
            "url_repository": "URL del Repositorio",
            "lenguajes": "Lenguajes/Tecnologías",
            "image": "Imagen del Proyecto",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.all()
        if not self.instance.pk:
            self.fields["image"].required = True
        else:
            self.fields["image"].required = False
        if self.instance and self.instance.lenguajes:
            self.initial["lenguajes"] = ", ".join(self.instance.lenguajes)

    def clean_lenguajes(self):
        lenguajes = self.cleaned_data.get("lenguajes", "")
        if lenguajes:
            lenguajes_list = [
                lang.strip() for lang in lenguajes.split(",") if lang.strip()
            ]
            return lenguajes_list
        return []

    def clean_image(self):
        image = self.cleaned_data.get("image", False)
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB máximo
                raise forms.ValidationError("La imagen no puede superar los 5MB")
        else:
            self.instance.pk and not image
            return self.instance.image
        return image
