# vim:fileencoding=utf-8
from services.models import Service
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin



class ServiceAdmin(AdminImageMixin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


admin.site.register(Service, ServiceAdmin)