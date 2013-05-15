# vim:fileencoding=utf-8
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class CakesApp(CMSApp):
    name = u'Услуги: Торты'
    urls = ["services.cake_urls"]


class DecoratesApp(CMSApp):
    name = u'Услуги: Украшения'
    urls = ["services.decorate_urls"]


class RequisitesApp(CMSApp):
    name = u'Услуги: Реквизиты'
    urls = ["services.req_urls"]


class ArtistApp(CMSApp):
    name = u'Услуги: Артисты'
    urls = ["services.artist_urls"]


class McApp(CMSApp):
    name = u'Услуги: Ведущие'
    urls = ["services.mc_urls"]


class KidsApp(CMSApp):
    name = u'Услуги: Для детей'
    urls = ["services.kids_urls"]


class MusicApp(CMSApp):
    name = u'Услуги: Музыканты'
    urls = ["services.music_urls"]


class CarApp(CMSApp):
    name = u'Услуги: Автомобили'
    urls = ["services.car_urls"]


apphook_pool.register(CakesApp)
apphook_pool.register(DecoratesApp)
apphook_pool.register(RequisitesApp)
apphook_pool.register(ArtistApp)
apphook_pool.register(McApp)
apphook_pool.register(KidsApp)
apphook_pool.register(MusicApp)
apphook_pool.register(CarApp)