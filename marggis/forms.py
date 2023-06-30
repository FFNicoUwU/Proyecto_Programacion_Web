from django import forms 
from .models import Genero, Contacto 

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = "__all__"


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'