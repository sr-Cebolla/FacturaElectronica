from django.shortcuts import render
from django.http import HttpResponse
from .models import Definicion
from .models import MedioAmbiente
from.models import Poblacion
from .models import EconomiaEmisores
from .models import Emisores
from .models import Informacion
import json

def index(request):
    definicion01 = Definicion.objects.get(pk=1)
    definicion02 = Definicion.objects.get(pk=2)
    definicion03 = Definicion.objects.get(pk=5)

    medio01 = MedioAmbiente.objects.get(pk=1)
    medio02 = MedioAmbiente.objects.get(pk=2)

    pob01 = Poblacion.objects.get(pk=1)
    pob02 = Poblacion.objects.get(pk=2)
    pob03 = Poblacion.objects.get(pk=3)
    pob04 = Poblacion.objects.get(pk=4)
    pob05 = Poblacion.objects.get(pk=5)

    eco01 = EconomiaEmisores.objects.get(pk=1)
    eco02 = EconomiaEmisores.objects.get(pk=2)
    eco03 = EconomiaEmisores.objects.get(pk=3)
    
    datos = Emisores.objects.all()
    fechas = [fecha.strftime('%Y-%m-%d') for fecha in datos.values_list('fecha', flat=True)]
    cantidades = [cantidad for cantidad in Emisores.objects.all().values_list('cantidad', flat=True)]

    reque01 = Informacion.objects.get(pk=1)
    reque02 = Informacion.objects.get(pk=2)
    reque03 = Informacion.objects.get(pk=3)
    reque04 = Informacion.objects.get(pk=4)
    reque05 = Informacion.objects.get(pk=5)
    reque06 = Informacion.objects.get(pk=6)


    context = {
        'definicion01' : definicion01,
        'definicion02' : definicion02,
        'definicion03' : definicion03,

        'medio01' : medio01,
        'medio02' : medio02,
        
        'pob01': pob01,
        'pob02': pob02,
        'pob03': pob03,
        'pob04': pob04,
        'pob05': pob05,
        'eco01' : eco01,
        'eco02' : eco02,
        'eco03' : eco03,

        'cantidad' : json.dumps(cantidades),
        'fechas' : json.dumps(fechas),

        'reque01' : reque01,
        'reque02' : reque02,
        'reque03' : reque03,
        'reque04' : reque04,
        'reque05' : reque05,
        'reque06' : reque06,

    }

    return render(request, 'index_usuario/index.html', context)


def login_view(request):
    return render(request, 'index_usuario/login.html')
# Create your views here.


