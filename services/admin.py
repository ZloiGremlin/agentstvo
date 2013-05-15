# vim:fileencoding=utf-8
from services.models import Service, Cake, Decoration, ImageInline, Color, ImageInlineReq, Requisite, CategoryCake
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
    list_display = ['thumb', 'name', 'price', 'weight', 'active']
    list_display_links = ['thumb', 'name']
    list_editable = ['active']

class CategoryCakeAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['thumb', 'name', 'sort']
    list_display_links = ['thumb', 'name']
    list_editable = ['sort']
    prepopulated_fields = {"url": ("name",)}

admin.site.register(Service, ServiceAdmin)
admin.site.register(Cake, CakeAdmin)
admin.site.register(Decoration, DecorationAdmin)
admin.site.register(Requisite, ReqAdmin)
admin.site.register(CategoryCake, CategoryCakeAdmin)
admin.site.register(Color)