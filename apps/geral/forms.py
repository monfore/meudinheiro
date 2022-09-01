from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        exclude = ['usuario']

