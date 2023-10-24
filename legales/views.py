from django.views import generic
from .models import Causa


class HomeView(generic.ListView):
    queryset = Causa.objects.all()
    context_object_name = 'causa_list'
    template_name = 'causaList.html'