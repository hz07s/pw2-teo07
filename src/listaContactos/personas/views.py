from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona

# Create your views here.
def personaTextView(request):
    obj = Persona.objects.get(id = 1)
    context = {
        'nombre' : obj.nomres,
        'edad' : obj.edad,
    }
    return render(request, 'personas/test.html', context)
