from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class PasswordChangeCustomForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            }
        ),
        label="Contraseña actual",
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            }
        ),
        label="Nueva contraseña",
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            }
        ),
        label="Confirmar nueva contraseña",
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")  # pasamos el usuario en la vista
        super().__init__(*args, **kwargs)

    def clean_current_password(self):
        current_password = self.cleaned_data.get("current_password")
        if not self.user.check_password(current_password):
            raise forms.ValidationError("La contraseña actual es incorrecta")
        return current_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Las contraseñas nuevas no coinciden")
        return cleaned_data

    def save(self, commit=True):
        new_password = self.cleaned_data["new_password"]
        self.user.set_password(new_password)
        if commit:
            self.user.save()
        return self.user
