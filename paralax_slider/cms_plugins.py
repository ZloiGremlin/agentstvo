# vim:fileencoding=utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from paralax_slider.models import ParalaxPlugin as ParalaxPluginModel
from paralax_slider.models import NivoPlugin as NivoPluginModel
from paralax_slider.models import GalleryPlugin as GalleryPluginModel
from django.utils.translation import ugettext as _

class ParalaxPlugin(CMSPluginBase):
    model = ParalaxPluginModel
    name = u'Паралакс слайдер'
    render_template = "paralax_slider/slider.html"

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

plugin_pool.register_plugin(ParalaxPlugin)


class NivoPlugin(CMSPluginBase):
    model = NivoPluginModel
    name = u'Nivo слайдер'
    render_template = "paralax_slider/nivo.html"

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

plugin_pool.register_plugin(NivoPlugin)


class GalleryPlugin(CMSPluginBase):
    model = GalleryPluginModel
    name = u'Галерея'
    render_template = "paralax_slider/gallery.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance, 'images':instance.album.images.all()[:instance.quantity]})
        return context

plugin_pool.register_plugin(GalleryPlugin)

