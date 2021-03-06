from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
import random
from .forms import RegModelForm, ContactForm
from .models import Registrados




# Create your views here.
def inicio(request):
    titulo="Bienvenidos"

    if request.user.is_authenticated:
        titulo =(" bienvenido %s" %(request.user)).upper()
    form= RegModelForm(request.POST or None)

    context = {
    "elf":form,
    "title":titulo,
    "tit":titulo,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")

        if not instance.nombre:
            instance.nombre="persona"
        instance.save()

        context = {
        "title":"Gracias %s!"%(nombre)
        }
        #esta linea sirve para tomar el nombre del usuario que esta activo en la pagina
#"title":"Gracias %s!"%(nombre)
        if not nombre:
            context={
            "title": "gracias %s!"%(email)
            }

        print(instance)
        print(instance.timestamp)


        #form_data = form.cleaned_data
        #abc= form_data.get("email")
        #abc2= form_data.get("nombre")
        #obj= Registrados.objects.create(email=abc,nombre=abc2)

        #queryset = Registrados.objects.all().order_by("-timestamp").filter(nombre__icontains="per")
    if request.user.is_authenticated and request.user.is_staff:
        queryset = Registrados.objects.all().order_by("-timestamp")
        # i=1
        # for instance in Registrados.objects.all():
            # print(i)
            # print(instance.nombre )

        context = {
             "prueba": queryset,
         }

    return render(request, "inicio.html",context)




def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():

############################################################################################
       #imprimir el display por medio de iteracion
        #for key,value in form.cleaned_data.iteritems():
            #print key,value
#-----------------------------------------------------------------------
        #imprimir el display por un ciclo
        #for key in form.cleaned_data:
             #print (key)
             #print (form.cleaned_data.get(key))

        #podemos cambiar todas las lineas de impresion por un ciclo que imprima todo el formulario
##########################################################################################################
        form_email= form.cleaned_data.get("email")
        form_mensaje= form.cleaned_data.get("mensaje")
        form_nombre= form.cleaned_data.get("nombre")
        asunto='form de contacto'
        email_from=settings.EMAIL_HOST_USER
        email_to =[email_from,"otroemail@gmail.com"]
        email_mensaje ="%s: %s enviado por %s" %(form_nombre,form_mensaje,form_email)
        send_mail(asunto,email_mensaje,email_from,email_to,fail_silently=False)


    context = {
               "form": form,
               }

    return render(request,"forms.html",context)
