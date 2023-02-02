from django.contrib import admin
from .models import Mascota, Adoptante, Solicitud


admin.site.register(Mascota)
admin.site.register(Adoptante)
admin.site.register(Solicitud)