from django.shortcuts import render
from .models import Parientes


def mostrar_parientes(request):

    mama = Parientes(nombre= "Maria", parentezco ="Mamá", fechanac= "1964-12-03", edad = 45)
    papa = Parientes(nombre= "Juan", parentezco = "Papá", fechanac= "1972-20-09", edad= 50)
    hermano = Parientes(nombre= "Carlos", parentezco = "Hermano", fechanac= "1992-05-08", edad= 30)

    return render(request, 'parientes.html', {'objetos': [mama, papa, hermano]})