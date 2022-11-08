from django.shortcuts import render
from .models import Parientes


def mostrar_parientes(request):

    mama = Parientes(nombre= "Maria", parentezco= "Madre", edad = 45)
    papa = Parientes(nombre= "Juan", parentezco= "Padre", edad= 50)
    hermano = Parientes(nombre= "Carlos", parentezco= "Hermano", edad= 30)

    return render(request, 'parientes.html', {'objetos': [mama, papa, hermano]})