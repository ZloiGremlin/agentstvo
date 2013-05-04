# vim:fileencoding=utf-8
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class CakesApp(CMSApp):
    name = u'Услуги: Торты'
    urls = ["services.cake_urls"]

apphook_pool.register(CakesApp)