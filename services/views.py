# Create your views here.
from django.views.generic import ListView
from services.models import Cake, Decoration


class Cakes(ListView):
    context_object_name = "list"
    paginate_by = 18
    template_name = 'services/cakes.html'

    def get_queryset(self):
        return Cake.objects.filter(active=True)


class Decorates(ListView):
    context_object_name = "list"
    paginate_by = 15
    template_name = 'services/decorates.html'

    def get_queryset(self):
        return Decoration.objects.filter(active=True)