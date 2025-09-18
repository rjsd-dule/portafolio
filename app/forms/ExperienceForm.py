from django import forms
from app.models import Experience
from datetime import date


class ExperienceForm(forms.ModelForm):
    current_job = forms.BooleanField(
        required=False,
        label="¿Es tu trabajo actual?",
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input", "onchange": "toggleEndDate(this)"}
        ),
    )

    class Meta:
        model = Experience
        fields = [
            "job_title",
            "sub_title",
            "company",
            "start_date",
            "end_date",
            "description",
            "is_current",
        ]

        # Mensajes de error personalizados en español
        error_messages = {
            "job_title": {"required": "Este campo es obligatorio"},
            "sub_title": {"required": "Este campo es obligatorio"},
            "company": {"required": "Este campo es obligatorio"},
            "start_date": {"required": "Debes proporcionar una fecha de inicio"},
            "end_date": {
                "required": "Debes proporcionar una fecha de fin si no es tu trabajo actual"
            },
            "description": {"required": "Este campo es obligatorio"},
        }

        widgets = {
            "job_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Desarrollador Full Stack",
                }
            ),
            "sub_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Especializado en Django y React",
                }
            ),
            "company": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Google, Microsoft, etc.",
                }
            ),
            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "max": date.today().isoformat(),
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "max": date.today().isoformat(),
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Describe tus responsabilidades y logros...",
                }
            ),
            "is_current": forms.HiddenInput(),
        }

        labels = {
            "job_title": "Puesto de Trabajo",
            "sub_title": "Subtítulo o Especialidad",
            "company": "Empresa",
            "start_date": "Fecha de Inicio",
            "end_date": "Fecha de Fin",
            "description": "Descripción",
            "is_current": "",
        }

        help_texts = {
            "sub_title": "Opcional - Especialización, departamento, etc.",
            "end_date": "Deja en blanco si es tu trabajo actual",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.is_current:
            self.fields["end_date"].required = False
            self.fields["end_date"].widget.attrs["disabled"] = True

        self.fields["current_job"].initial = (
            self.instance.is_current if self.instance else False
        )

    def clean_start_date(self):
        start_date = self.cleaned_data.get("start_date")
        if start_date and start_date > date.today():
            raise forms.ValidationError("La fecha de inicio no puede ser futura")
        return start_date

    def clean_end_date(self):
        end_date = self.cleaned_data.get("end_date")
        if end_date and end_date > date.today():
            raise forms.ValidationError("La fecha de fin no puede ser futura")
        return end_date

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        is_current = cleaned_data.get("current_job", False)

        if is_current:
            cleaned_data["end_date"] = None
        else:
            if not end_date:
                self.add_error(
                    "end_date",
                    "Debes proporcionar una fecha de fin si no es tu trabajo actual",
                )

        if start_date and end_date and not is_current:
            if end_date < start_date:
                self.add_error(
                    "end_date",
                    "La fecha de fin debe ser posterior a la fecha de inicio",
                )

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.is_current = self.cleaned_data.get("current_job", False)

        if commit:
            instance.save()
        return instance
