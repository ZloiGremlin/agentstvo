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
    category = models.ForeignKey('CategoryCake', verbose_name=u'Категория', blank=True, null=True)
    active = models.BooleanField(verbose_name=u'Отображение', default=True)

    def __unicode__(self):
        return self.name

    def thumb(self):
        im = get_thumbnail(self.image, '70x70', crop='center', quality=100)
        return '<img src="%s">' % im.url
    thumb.allow_tags = True
    thumb.short_description = u'Фото'


class CategoryCake(models.Model):
    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории Тортов'
        ordering = ['sort']

    name = models.CharField(max_length=255, verbose_name=u'Название')
    url = models.SlugField(unique=True, max_length=255, verbose_name=u'Адрес')
    description = models.TextField(max_length=255, verbose_name=u'Описание', blank=True, null=True)
    image = ImageField(upload_to=get_file_path, verbose_name=u'Фото')
    sort = models.IntegerField(verbose_name=u'Приоритет', default=100)

    def __unicode__(self):
        return self.name

    def thumb(self):
        im = get_thumbnail(self.image, '70x70', crop='center', quality=100)
        return '<img src="%s">' % im.url
    thumb.allow_tags = True
    thumb.short_description = u'Фото'


class Decoration(models.Model):
    class Meta:
        verbose_name = u'Украшение'
        verbose_name_plural = u'Украшения'
        ordering = ['price']

    name = models.CharField(max_length=255, verbose_name=u'Название')
    description = models.TextField(max_length=255, verbose_name=u'Описание', blank=True, null=True)
    price = models.IntegerField(verbose_name=u'Цена', default=0)
    active = models.BooleanField(verbose_name=u'Отображение', default=True)

    def __unicode__(self):
        return self.name

    def get_first_color(self):
        q = self.images.all()
        if q.count() > 0:
            return q[0]
        else:
            return None

    def get_thumbs(self):
        return self.images.filter(color=None)

    def thumb(self):
        if self.get_first_color():
            im = get_thumbnail(self.get_first_color().image, '70x70', crop='center', quality=100)
            return '<img src="%s">' % im.url
        else:
            return None
    thumb.allow_tags = True
    thumb.short_description = u'Фото'


class Requisite(models.Model):
    class Meta:
        verbose_name = u'Реквизит'
        verbose_name_plural = u'Реквизиты'
        ordering = ['price']

    name = models.CharField(max_length=255, verbose_name=u'Название')
    description = models.TextField(max_length=255, verbose_name=u'Описание', blank=True, null=True)
    price = models.IntegerField(verbose_name=u'Цена', default=0)
    color = models.ManyToManyField('Color', max_length=255, verbose_name=u'Цветовая гамма', blank=True, null=True)
    active = models.BooleanField(verbose_name=u'Отображение', default=True)

    def __unicode__(self):
        return self.name

    def get_first_image(self):
        q = self.images.all()
        if q.count() > 0:
            return q[0]
        else:
            return None

    def thumb(self):
        if self.get_first_image():
            im = get_thumbnail(self.get_first_image().image, '70x70', crop='center', quality=100)
            return '<img src="%s">' % im.url
        else:
            return None
    thumb.allow_tags = True
    thumb.short_description = u'Фото'


class Color(models.Model):
    class Meta:
        verbose_name = u'Цвет'
        verbose_name_plural = u'Цвета'
        ordering = ['name']

    name = models.CharField(max_length=255, verbose_name=u'Название')
    rgb = models.CharField(max_length=255, verbose_name=u'Код цвета')

    def __unicode__(self):
        return self.name


class ImageInline(models.Model):
    class Meta:
        verbose_name = u'Фото'
        verbose_name_plural = u'Фото'

    image = ImageField(upload_to=get_file_path, verbose_name=u'Фото')
    color = models.ForeignKey(Color, max_length=255, verbose_name=u'Цвет', blank=True, null=True)
    decoration = models.ForeignKey(Decoration, max_length=255, verbose_name=u'Украшение', related_name='images')
    sort = models.IntegerField(verbose_name=u'Приоритет', default=100)


class ImageInlineReq(models.Model):
    class Meta:
        verbose_name = u'Фото'
        verbose_name_plural = u'Фото'

    image = ImageField(upload_to=get_file_path, verbose_name=u'Фото')
    requisite = models.ForeignKey(Requisite, max_length=255, verbose_name=u'Украшение', related_name='images')
    sort = models.IntegerField(verbose_name=u'Приоритет', default=100)