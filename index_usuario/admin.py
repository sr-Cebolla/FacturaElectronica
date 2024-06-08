from django.contrib import admin
from .models import Administrador, Definicion, EconomiaEmisores, Poblacion, MedioAmbiente, MetodoEvacion, EvacionImpuestos, Efectos, Emisores, Informacion

admin.site.register(Administrador)
admin.site.register(Definicion)
admin.site.register(EconomiaEmisores)
admin.site.register(Poblacion)
admin.site.register(MedioAmbiente)
admin.site.register(MetodoEvacion)
admin.site.register(EvacionImpuestos)
admin.site.register(Efectos)
admin.site.register(Emisores)
admin.site.register(Informacion)
