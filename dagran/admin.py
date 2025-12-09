from django.contrib import admin
from .models import Alerta, Nivel_alerta, Reporte
from django.conf import settings

# Register your models here.

admin.site.register(Alerta)
admin.site.register(Nivel_alerta)
admin.site.register(Reporte)