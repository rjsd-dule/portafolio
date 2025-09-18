from django import forms
from app.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
        labels={
            'name': 'Nombre de la categoría'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe el nombre de la categoría'
            })
        }