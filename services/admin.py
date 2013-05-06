# vim:fileencoding=utf-8
from services.models import Service, Cake, Decoration, ImageInline, Color
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin, AdminInlineImageMixin

class ImageInlineAdmin(AdminInlineImageMixin, admin.TabularInline):
    model = ImageInline
    extra = 2

class DecorationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['thumb', 'name', 'price', 'active']
    list_display_links = ['thumb', 'name']
    list_editable = ['active']
    inlines = [ImageInlineAdmin]

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
admin.site.register(Decoration, DecorationAdmin)
admin.site.register(Color)