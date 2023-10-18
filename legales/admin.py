from django.contrib import admin
from .models import Company, Jurisdiccion, Abogado, BonoJus, Excepcion, \
                    EstadoProcesal, ObservacionPMP, EstadoNegociacion, \
                    ObservacionPericia, Causa

admin.site.register(Company, admin.ModelAdmin)
admin.site.register(Jurisdiccion, admin.ModelAdmin)
admin.site.register(Abogado, admin.ModelAdmin)
admin.site.register(BonoJus, admin.ModelAdmin)
admin.site.register(Excepcion, admin.ModelAdmin)
admin.site.register(EstadoProcesal, admin.ModelAdmin)
admin.site.register(ObservacionPMP, admin.ModelAdmin)
admin.site.register(EstadoNegociacion, admin.ModelAdmin)
admin.site.register(ObservacionPericia, admin.ModelAdmin)
admin.site.register(Causa, admin.ModelAdmin)
