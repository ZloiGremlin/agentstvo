# vim:fileencoding=utf-8
from cms.models import Page, CMSPlugin
from sorl.thumbnail import ImageField
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
