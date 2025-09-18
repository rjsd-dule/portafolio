from django import forms
from app.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "email",
            "nombre",
            "apellido",
            "telefono",
            "bio",
            "profesion",
            "profile_document",
            "profile_picture",
            "website",
            "url_repository",
            "url_linkedin",
        ]
