from django.shortcuts import render
from .models import Mascota
# Create your views here.


def index(request):
    #mascotas = Mascota.objects.all()
    mascotas = Mascota.objects.filter(adoptado=False)
    return render(request, 'mascotas.html', {'mascotas': mascotas})

def get_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    return render(request, 'mascota.html', {'mascota': mascota})
