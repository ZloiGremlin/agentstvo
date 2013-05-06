# vim:fileencoding=utf-8
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class CakesApp(CMSApp):
    name = u'Услуги: Торты'
    urls = ["services.cake_urls"]


class DecoratesApp(CMSApp):
    name = u'Услуги: Украшения'
    urls = ["services.decorate_urls"]


apphook_pool.register(CakesApp)
apphook_pool.register(DecoratesApp)