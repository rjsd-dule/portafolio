from django import forms
from app.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(
        widget=forms.PasswordInput, label="Confirmar contraseña"
    )

    class Meta:
        model = User
        fields = ["email", "nombre", "apellido", "telefono"]

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email
        user.set_password(self.cleaned_data["password"])  # encriptar contraseña
        if commit:
            user.save()
        return user
