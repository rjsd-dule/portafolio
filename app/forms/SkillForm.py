from django import forms
from app.models import Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = [
            "name",
            "level",
            "category",
            "skill_type",
            "certification",
            "example",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Python, Comunicación, Liderazgo",
                    "autocomplete": "off",
                }
            ),
            "level": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "max": 10,
                    "type": "number",
                    "oninput": 'validity.valid||(value="");',
                }
            ),
            "skill_type": forms.Select(attrs={"class": "form-control"}),
            "certification": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Certificación AWS, Curso de Scrum",
                }
            ),
            "example": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Ej: Desarrollé una API REST con Django REST Framework...",
                    "style": "resize: vertical;",
                }
            ),
        }

        help_texts = {
            "level": "Nivel entre 1 (básico) y 10 (experto)",
            "certification": "Opcional - Si tienes alguna certificación relacionada",
            "example": "Opcional - Describe un ejemplo concreto de aplicación",
        }

    def clean_level(self):
        level = self.cleaned_data.get("level")
        if level and (level < 1 or level > 10):
            raise forms.ValidationError("El nivel debe estar entre 1 y 10")
        return level
