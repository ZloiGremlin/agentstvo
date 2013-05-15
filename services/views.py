# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from services.models import Cake, Decoration, Requisite, CategoryCake, Artist


class Cakes(ListView):
    context_object_name = "list"
    paginate_by = 18
    template_name = 'services/cakes.html'

    def get_queryset(self):
        cat = get_object_or_404(CategoryCake, url=self.kwargs['slug'])
        return Cake.objects.filter(active=True, category=cat)

class CategoryCakes(ListView):
    context_object_name = "list"
    template_name = 'services/category-cakes.html'

    def get_queryset(self):
        return CategoryCake.objects.all()


class Decorates(ListView):
    context_object_name = "list"
    paginate_by = 15
    template_name = 'services/decorates.html'

    def get_queryset(self):
        return Decoration.objects.filter(active=True)


class Requisites(ListView):
    context_object_name = "list"
    paginate_by = 15
    template_name = 'services/requisites.html'

    def get_queryset(self):
        return Requisite.objects.filter(active=True)


class ArtistList(ListView):
    context_object_name = "list"
    paginate_by = 15
    type_artist = 'artist'
    template_name = 'services/artists.html'

    def get_queryset(self):
        return Artist.objects.filter(active=True, type=self.type_artist)