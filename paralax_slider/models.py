# vim:fileencoding=utf-8
from sorl.thumbnail import ImageField
from django.db import models
from agentstvo.utils import get_file_path
from django.db.models import permalink
from django.db.models import Min
from cms.models import CMSPlugin

class ParalaxPlugin(CMSPlugin):
    album = models.ForeignKey('gallery.AlbumImage', related_name='plugins', verbose_name=u'Альбом')

    def __unicode__(self):
        return self.album.name

    def copy_relations(self, oldinstance):
        self.album.images = oldinstance.album.images.all()

class NivoPlugin(CMSPlugin):
    album = models.ForeignKey('gallery.AlbumImage', related_name='nivo', verbose_name=u'Альбом')

    def __unicode__(self):
        return self.album.name

    def copy_relations(self, oldinstance):
        self.album.images = oldinstance.album.images.all()


class GalleryPlugin(CMSPlugin):
    album = models.ForeignKey('gallery.AlbumImage', related_name='lightbox', verbose_name=u'Альбом')
    quantity = models.IntegerField(verbose_name=u'Количество фото', default=10)

    def __unicode__(self):
        return self.album.name

    def copy_relations(self, oldinstance):
        self.album.images = oldinstance.album.images.all()[:self.quantity]