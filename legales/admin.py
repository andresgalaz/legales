from django.contrib import admin
from django.db.models.functions import Lower
from .models import Company, Jurisdiccion, Abogado, BonoJus, Excepcion, \
                    EstadoProcesal, ObservacionPMP, EstadoNegociacion, \
                    ObservacionPericia, Causa, TipoProceso, \
                    Vencimiento, TipoVencimiento, ExcepcionCausa


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


class VencimientoInline(admin.TabularInline):
    model = Vencimiento


class ExcepcionCausaInline(admin.TabularInline):
    model = ExcepcionCausa


class CausaAdmin(admin.ModelAdmin):
    list_display = ('company', 'asunto', 'caratula', 'estado_procesal', 'estado_negociacion')
    search_fields = ('asunto', 'caratula')
    list_filter = ('estado_procesal', 'estado_negociacion', )
    inlines = [VencimientoInline, ExcepcionCausaInline, ]


admin.site.site_header = 'B&A Consultores'
admin.site.site_title = 'Legales'
admin.site.register(Abogado, AbogadoAdmin)
admin.site.register(BonoJus, SimpleAdmin)
admin.site.register(Causa, CausaAdmin)
admin.site.register(Company, SimpleAdmin)
admin.site.register(EstadoNegociacion, SimpleAdmin)
admin.site.register(EstadoProcesal, SimpleAdmin)
admin.site.register(Excepcion, SimpleAdmin)
admin.site.register(Jurisdiccion, SimpleAdmin)
admin.site.register(ObservacionPericia, SimpleAdmin)
admin.site.register(ObservacionPMP, SimpleAdmin)
# admin.site.register(Oficio, SimpleAdmin)
admin.site.register(TipoProceso, SimpleAdmin)
admin.site.register(TipoVencimiento, SimpleAdmin)
