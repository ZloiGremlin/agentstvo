# vim:fileencoding=utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from paralax_slider.models import ParalaxPlugin as ParalaxPluginModel
from django.utils.translation import ugettext as _

class ParalaxPlugin(CMSPluginBase):
    model = ParalaxPluginModel
    name = u'Паралакс слайдер'
    render_template = "paralax_slider/slider.html"

    def render(self, context, instance, placeholder):
        context.update({'instance':instance})
        return context

plugin_pool.register_plugin(ParalaxPlugin)