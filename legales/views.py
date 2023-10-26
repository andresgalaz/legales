from django import forms
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView

from .models import Vencimiento

class HomeFilterForm(forms.Form):
    data = [(None, 'Todas')]

class HomeView(FormMixin, ListView):
    queryset = Vencimiento.objects.all()
    context_object_name = 'causa_list'
    template_name = 'causaList.html'
    model = Vencimiento
    paginate_by = 50

    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = HomeFilterForm(self.request.GET)
        return context
