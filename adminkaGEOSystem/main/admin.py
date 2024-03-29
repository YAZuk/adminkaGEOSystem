from django.contrib import admin
from .models import Transport, Company, Device, Act
from django.utils.safestring import mark_safe


# Register your models here.

class AdminAct(admin.ModelAdmin):
    fields = ['executor', 'description', 'transport', 'add_date']
    list_display = ['executor', 'description', 'transport', 'add_date']
    # readonly_fields = ['add_date']


class AdminTransport(admin.ModelAdmin):
    fields = ['name', 'vin', 'company', 'device', 'add_date', 'transport_img']
    list_display = ['name', 'vin', 'company', 'device', 'add_date']
    readonly_fields = ['add_date', 'preview']
    search_fields = ['name', 'vin', ]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}">')


class AdminCompany(admin.ModelAdmin):
    fields = ['name', 'add_date']
    list_display = ['name', 'add_date']
    readonly_fields = ['add_date']


class AdminDevice(admin.ModelAdmin):
    fields = ['imei', 'name', 'add_date']
    list_display = ['imei', 'name', 'add_date']
    readonly_fields = ['add_date']


admin.site.register(Transport, AdminTransport)
admin.site.register(Company, AdminCompany)
admin.site.register(Device, AdminDevice)
admin.site.register(Act, AdminAct)
