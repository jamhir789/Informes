from django.shortcuts import render
from .forms import RegForm
from .models import Registrados
# Create your views here.
def inicio(request):
    titulo="hola"
    form= RegForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        abc= form_data.get("email")
        abc2= form_data.get("nombre")
        obj= Registrados.objects.create(email=abc,nombre=abc2)



    context = {
    "elf":form,
    "title":titulo,
    }
    return render(request, "inicio.html",context)
