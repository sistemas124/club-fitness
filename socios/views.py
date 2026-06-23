from django.shortcuts import render

def ver_plantilla(request):
    # Cambiamos 'plantillaprincipal.html' por 'inicio.html'
    return render(request, 'inicio.html')