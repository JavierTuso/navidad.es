from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request,'nosotros.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def privacidad(request):
    return render(request, 'privacidad.html')

def copyright(request):
    return render(request, 'copyright.html')

def expofunsa(request):
    return render(request, 'expofunsa.html')

def registrarse(request):
    return render(request,'registrarse.html')

def hospedaje(request):
    return render(request, 'hospedaje.html')

def contacto(request):
    return render(request,'contacto.html')

def ubicacion(request):
    return render(request,'ubicacion.html')

def navidad(request):
    return render(request,'navidad.html')

def fiestasPatrias(request):
    return render(request,'fiestasPatrias.html')

def otrasFiestas(request):
    return render(request,'otrasFiestas.html')
# Create your views here.
