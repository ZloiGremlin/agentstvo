# vim:fileencoding=utf-8
from cms.models import Page, CMSPlugin
from sorl.thumbnail import ImageField, get_thumbnail
from django.db import models
from agentstvo.utils import get_file_path
from django.db.models import permalink
from django.db.models import Min


class Service(models.Model):
    class Meta:
        verbose_name = u'Услуга'
        verbose_name_plural = u'Услуги'
        ordering = ['-sort']

    name = models.CharField(max_length=255, verbose_name=u'Название')
    teaser = models.TextField(max_length=255, verbose_name=u'Описание')
    page = models.ForeignKey(Page, verbose_name=u'Ссылка на страницу')
    image = ImageField(upload_to=get_file_path, verbose_name=u'Иконка')
    sort = models.IntegerField(verbose_name=u'Приоритет', default=100)

    def __unicode__(self):
        return self.name


class ServicePlugin(CMSPlugin):
    name = models.CharField(max_length=255, verbose_name=u'Заголовок')
    display = models.BooleanField(verbose_name=u'Отображать заголовок', default=False)
    service = models.ManyToManyField('Service', related_name='plugins', verbose_name=u'Услуги')

    def __unicode__(self):
        return self.name

    def copy_relations(self, oldinstance):
        self.service = oldinstance.service.all()

class Cake(models.Model):
    class Meta:
        verbose_name = u'Торт'
        verbose_name_plural = u'Торты'
        ordering = ['price']

    name = models.CharField(max_length=255, verbose_name=u'Название')
    weight = models.CharField(max_length=255, verbose_name=u'Вес', blank=True, null=True)
    description = models.TextField(max_length=255, verbose_name=u'Описание', blank=True, null=True)
    price = models.IntegerField(verbose_name=u'Цена за килограмм', default=0)
    image = ImageField(upload_to=get_file_path, verbose_name=u'Фото')
    active = models.BooleanField(verbose_name=u'Отображение', default=True)

    def __unicode__(self):
        return self.name

    def thumb(self):
        im = get_thumbnail(self.image, '70x70', crop='center', quality=100)
        return '<img src="%s">' % im.url
    thumb.allow_tags = True
    thumb.short_description = u'Фото'