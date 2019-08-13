from django.contrib import admin
from .models import Efemeride


# Register your models here.
class EfemerideAdmin(admin.ModelAdmin):
    list_display = ("id", "dia", "cita")
    ordering = ('dia',)


admin.site.site_header = "Efemerides Backend"
admin.site.register(Efemeride, EfemerideAdmin)
