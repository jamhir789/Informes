from django.contrib import admin
from .forms import RegModelForm
from .models import Registrados


#añadir los demas campos al display
class AdminRegistrado(admin.ModelAdmin):
    list_display =["email","nombre","timestamp"]
    form= RegModelForm
    #list_display_links=["nombre"]
    list_filter=["timestamp"]
    list_editable =["nombre"]
    search_fields=["email","nombre"]
    #class Meta:
        #model=Registrados

# Register your models here.
admin.site.register(Registrados,AdminRegistrado)
