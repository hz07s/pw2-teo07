from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fiels = [
            'nombres',
            'apellidos',
            'edad',
            'donador'
        ]