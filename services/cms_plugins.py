# vim:fileencoding=utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from services.models import ServicePlugin as ServicePluginModel
from django.utils.translation import ugettext as _


class ServicePlugin(CMSPluginBase):
    model = ServicePluginModel
    name = u'Блок услуг'
    render_template = "services/services.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(ServicePlugin)