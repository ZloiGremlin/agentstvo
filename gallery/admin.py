# vim:fileencoding=utf-8
from gallery.models import AlbumImage, Image
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin


class AdminInlineImage(AdminImageMixin, admin.TabularInline):
    model = Image
    extra = 10


class AlbumAdmin(AdminImageMixin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    inlines = [AdminInlineImage]


admin.site.register(AlbumImage, AlbumAdmin)