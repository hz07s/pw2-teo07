from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

# Create your views here.
def personaTextView(request):
    obj = Persona.objects.get(id = 1)
    context = {
        'objeto' : obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personaCreateView(request):
    forms = PersonaForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        form = PersonaForm()

    context = {
            'form' : form 
        }
    return render(request, 'personas/personasCreate.html', context)