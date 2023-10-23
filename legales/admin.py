from django.contrib import admin
from django.db.models.functions import Lower
from .models import Company, Jurisdiccion, Abogado, BonoJus, Excepcion, \
                    EstadoProcesal, ObservacionPMP, EstadoNegociacion, \
                    ObservacionPericia, Causa, Oficio


class AbogadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo')
    search_fields = ('nombre', 'correo')

    def get_ordering(self, request):
        return [Lower('nombre')]


class SimpleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'id')
    search_fields = ('nombre', )

    def get_ordering(self, request):
        return [Lower('nombre')]


admin.site.site_header = 'B&A Consultores'
admin.site.site_title = 'Legales'
admin.site.register(Company, SimpleAdmin)
admin.site.register(Jurisdiccion, SimpleAdmin)
admin.site.register(Abogado, AbogadoAdmin)
admin.site.register(BonoJus, SimpleAdmin)
admin.site.register(Excepcion, SimpleAdmin)
admin.site.register(Oficio, SimpleAdmin)
admin.site.register(EstadoProcesal, SimpleAdmin)
admin.site.register(ObservacionPMP, SimpleAdmin)
admin.site.register(EstadoNegociacion, SimpleAdmin)
admin.site.register(ObservacionPericia, SimpleAdmin)
admin.site.register(Causa, admin.ModelAdmin)
