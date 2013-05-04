# Create your views here.
from django.views.generic import ListView
from services.models import Cake


class Cakes(ListView):
    context_object_name = "list"
    paginate_by = 18
    template_name = 'services/cakes.html'

    def get_queryset(self):
        return Cake.objects.filter(active=True)
