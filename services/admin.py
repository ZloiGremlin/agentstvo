# vim:fileencoding=utf-8
from services.models import Service, Cake
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin



class ServiceAdmin(AdminImageMixin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']

class CakeAdmin(AdminImageMixin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['thumb', 'name', 'price', 'weight', 'active']
    list_display_links = ['thumb', 'name']
    list_editable = ['active']

admin.site.register(Service, ServiceAdmin)
admin.site.register(Cake, CakeAdmin)