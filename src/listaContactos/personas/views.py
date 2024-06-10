from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona

# Create your views here.
def personaTextView(request):
    obj = Persona.objects.get(id = 1)
    context = {
        'nombre' : obj.nombres,
        'edad' : obj.edad,
    }
    return render(request, 'test.html', context)
