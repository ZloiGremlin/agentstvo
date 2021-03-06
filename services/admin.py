# vim:fileencoding=utf-8
from services.models import Service, Cake, Decoration, ImageInline, Color, ImageInlineReq, Requisite, CategoryCake, Artist, Car
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin, AdminInlineImageMixin




class ImageInlineAdmin(AdminInlineImageMixin, admin.TabularInline):
    model = ImageInline
    extra = 2


class ImageInlineReqAdmin(AdminInlineImageMixin, admin.TabularInline):
    model = ImageInlineReq
    extra = 2


class DecorationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['thumb', 'name', 'price', 'active']
    list_display_links = ['thumb', 'name']
    list_editable = ['active']
    inlines = [ImageInlineAdmin]


class ReqAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['thumb', 'name', 'price', 'active']
    list_display_links = ['thumb', 'name']
    list_editable = ['active']
    inlines = [ImageInlineReqAdmin]
    filter_horizontal = ['color']


class ServiceAdmin(AdminImageMixin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


class CakeAdmin(AdminImageMixin, admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['category']
    list_display = ['thumb', 'name', 'price', 'weight', 'active', 'category']
    list_display_links = ['thumb', 'name']
    list_editable = ['active', 'category']


class CategoryCakeAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['thumb', 'name', 'sort']
    list_display_links = ['thumb', 'name']
    list_editable = ['sort']
    prepopulated_fields = {"url": ("name",)}


class ArtistAdmin(AdminImageMixin, admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['type']
    list_display = ['thumb', 'name', 'price', 'active', 'type']
    list_display_links = ['thumb', 'name']
    list_editable = ['active', 'type']


class CarAdmin(AdminImageMixin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['thumb', 'name', 'price', 'active']
    list_display_links = ['thumb', 'name']
    list_editable = ['active']

admin.site.register(Service, ServiceAdmin)
admin.site.register(Cake, CakeAdmin)
admin.site.register(Decoration, DecorationAdmin)
admin.site.register(Requisite, ReqAdmin)
admin.site.register(CategoryCake, CategoryCakeAdmin)
admin.site.register(Color)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Car, CarAdmin)