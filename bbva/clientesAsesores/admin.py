from django.contrib import admin

# Register your models here.
from .models import Clientes, Asesores

admin.site.register(Clientes)
admin.site.register(Asesores)
