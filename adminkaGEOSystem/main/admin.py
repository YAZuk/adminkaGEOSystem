from django.contrib import admin
from .models import Transport


# Register your models here.

class AdminTransport(admin.ModelAdmin):
    fields = ['name', 'vin', 'add_date']
    readonly_fields = ['add_date']




admin.site.register(Transport, AdminTransport)
