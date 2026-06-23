from django.shortcuts import render

def ver_plantilla(request):
    return render(request, 'plantillaprincipal.html')