# vim:fileencoding=utf-8
from sorl.thumbnail import ImageField
from django.db import models
from agentstvo.utils import get_file_path
from django.db.models import permalink
from django.db.models import Min


class AlbumImage(models.Model):
    class Meta:
        verbose_name = u'Альбом'
        verbose_name_plural = u'Альбомы'

    name = models.CharField(max_length=255, verbose_name=u'Название альбома')

    def __unicode__(self):
        return self.name


class Image(models.Model):
    class Meta:
        verbose_name = u'Фото'
        verbose_name_plural = u'Фото'

    image = ImageField(upload_to=get_file_path, verbose_name=u'Изображение')
    title = models.CharField(max_length=255, verbose_name=u'Название', null=True, blank=True)
    sort = models.IntegerField(default=0, verbose_name=u'Приоритет')
    album = models.ForeignKey(AlbumImage, related_name='images')
