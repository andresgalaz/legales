from django import forms
from django.db.models import Q
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from dateutil.relativedelta import relativedelta
import datetime

from .models import Vencimiento


class HomeFilterForm(forms.Form):
    fecInicio = forms.DateField(label='Fecha Inicio', required=True,
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    fecFinal = forms.DateField(label='Fecha Final', required=True,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecInicio'].initial = datetime.date.today() - relativedelta(days=1)
        self.fields['fecInicio'].widget.attrs['value'] = self.fields['fecInicio'].initial
        self.fields['fecFinal'].initial = datetime.date.today() + relativedelta(days=7)
        self.fields['fecFinal'].widget.attrs['value'] = self.fields['fecFinal'].initial


class HomeView(FormMixin, ListView):
    context_object_name = 'vencimiento_list'
    form_class = HomeFilterForm
    model = Vencimiento
    paginate_by = 50
    queryset = Vencimiento.objects.all()
    template_name = 'vencimientoList.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = HomeFilterForm(self.request.GET)
        return context

    def querysetWrap(self, prmFecInicio, prmFecFinal):
        # prepare filters to apply to queryset
        filters = {}
        if prmFecInicio:
            filters['fecha__gte'] = prmFecInicio
        else:
            filters['fecha__gte'] = datetime.date.today() - relativedelta(days=1)
        if prmFecFinal:
            filters['fecha__lte'] = prmFecFinal
        else:
            filters['fecha__lte'] = datetime.date.today() + relativedelta(days=7)

        if len(filters) == 0:
            # Genera una salida vacía, se debe seleccionar planta
            return Vencimiento.objects.filter(fecha__year=1900)

        return Vencimiento.objects.filter(Q(**filters)).order_by('fecha')
        # .order_by( '-activo__fecha_ingreso', 'activo__tipoActivo')

    def get_queryset(self):
        return self.querysetWrap(self.request.GET.get('fecInicio'),
                                 self.request.GET.get('fecFinal'))
