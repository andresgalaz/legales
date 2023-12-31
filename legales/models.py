from django import forms
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ModifiedArrayField(ArrayField):
    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
            **kwargs
        }
        return super(ArrayField, self).formfield(**defaults)


class Company(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        unique_together = [['nombre',]]

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class Jurisdiccion(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        unique_together = [['nombre',]]

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class Abogado(models.Model):
    nombre = models.CharField(max_length=120)
    correo = models.CharField(max_length=120, blank=True, null=True)
    telefono1 = models.CharField(max_length=120, blank=True, null=True)
    telefono2 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        unique_together = [['nombre',]]

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class BonoJus(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        unique_together = [['nombre',]]

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class TipoProceso(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        unique_together = [['nombre',]]

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre

# class Oficio(models.Model):
#     nombre = models.CharField(max_length=20)
#     class Meta:
#         unique_together = [['nombre',]]
#     def __str__(self):
#         return str(self.id) + ' - ' + self.nombre


class EstadoProcesal(models.Model):
    nombre = models.CharField(max_length=40)

    class Meta:
        unique_together = [['nombre',]]

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class ObservacionPMP(models.Model):
    nombre = models.CharField(max_length=80)

    class Meta:
        unique_together = [['nombre',]]

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class EstadoNegociacion(models.Model):
    nombre = models.CharField(max_length=40)

    class Meta:
        unique_together = [['nombre',]]

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class ObservacionPericia(models.Model):
    nombre = models.CharField(max_length=80)

    class Meta:
        unique_together = [['nombre',]]

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class Causa(models.Model):
    LABEL_OFICIOS = (
        ("AFIP", "AFIP"),
        ("CENTRO MEDICO", "CENTRO MEDICO"),
        ("CORREO", "CORREO"),
        ("EMPLEADOR", "EMPLEADOR"),
        ("JUZGADO", "JUZGADO"),
        ("SRT", "SRT"),
        ("TRIBUNAL", "TRIBUNAL"),
    )
    fecha_derivacion = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    asunto = models.IntegerField()
    caratula = models.CharField(max_length=280)
    expediente = models.CharField(max_length=40)
    jurisdiccion = models.ForeignKey(Jurisdiccion, on_delete=models.CASCADE)
    tribunal = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    tipo_proceso = models.ForeignKey(TipoProceso, on_delete=models.CASCADE)
    fecha_inicio_demanda = models.DateField(null=True, blank=True)
    incapacidad_reclamada = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    lesiones_reclamada = models.CharField(max_length=380, blank=True, null=True)
    reclama_dano_sicologico = models.BooleanField(default=False, null=True)
    monto_demanda = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    fecha_pmi = models.DateField(null=True, blank=True)
    porcentaje_srt = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    abogado = models.ForeignKey(Abogado, on_delete=models.CASCADE)
    bono_y_jus = models.ForeignKey(BonoJus, on_delete=models.CASCADE)
    monto_jus = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    monto_bono = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    detalle = models.CharField(max_length=280, blank=True, null=True)
    preexistencia = models.DecimalField(max_digits=14, decimal_places=2, default=0, null=True, blank=True)
    estado_procesal = models.ForeignKey(EstadoProcesal, models.SET_NULL, blank=True, null=True)
    negociable_pmo = models.BooleanField(default=False, null=True)
    negociable_pmp = models.BooleanField(default=False, null=True)
    observacion_pericia = models.CharField(max_length=120, blank=True, null=True)
    fecha_pedido_pmp = models.DateField(null=True, blank=True)
    fecha_asigno_pmp = models.DateField(null=True, blank=True)
    fecha_pmp = models.DateField(null=True, blank=True)
    porcentaje_pmp = models.DecimalField(max_digits=14, decimal_places=2, default=0, null=True, blank=True)
    monto_autorizado = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    estado_negociacion = models.ForeignKey(EstadoNegociacion, models.SET_NULL, blank=True, null=True)
    ofrecimiento = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    contra_oferta = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    fecha_ultimo_ofrecimiento = models.DateField(null=True, blank=True)
    monto_acuerdo = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    fecha_presentacion_acuerdo = models.DateField(null=True, blank=True)
    hay_cbu = models.BooleanField(default=False, null=True)
    homologado = models.BooleanField(default=False, null=True)
    fecha_pedido_fondos = models.DateField(null=True, blank=True)
    fecha_venci_pago = models.DateField(null=True, blank=True)
    observacion = models.CharField(max_length=120, blank=True, null=True)
    ppmed = models.CharField(max_length=60, blank=True, null=True)
    ppsic = models.CharField(max_length=60, blank=True, null=True)
    pcont = models.CharField(max_length=60, blank=True, null=True)
    # oficios = models.ForeignKey(Oficio, models.SET_NULL, blank=True, null=True)
    oficios = ModifiedArrayField(
        models.CharField(
            choices=LABEL_OFICIOS,
            max_length=100,
            blank=True,
            null=True
        ),
        blank=True,
        null=True
    )
    confesional = models.BooleanField(default=False, null=True)
    testimonial = models.BooleanField(default=False, null=True)
    otras_pruebas = models.CharField(max_length=60, blank=True, null=True)
    sentencia = models.CharField(max_length=60, blank=True, null=True)
    pedido_fondos = models.CharField(max_length=60, blank=True, null=True)
    fecha_facturado = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = [['asunto',]]

    def __str__(self):
        return self.company.nombre + ' ' + str(self.asunto) + ' ' + self.caratula


class TipoVencimiento(models.Model):
    nombre = models.CharField(max_length=40)

    class Meta:
        unique_together = [['nombre',]]

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class Vencimiento(models.Model):
    fecha = models.DateField()
    causa = models.ForeignKey(Causa, on_delete=models.CASCADE)
    tipoVencimiento = models.ForeignKey(TipoVencimiento,
                                        on_delete=models.CASCADE)

    class Meta:
        unique_together = [['fecha', 'causa', 'tipoVencimiento']]

    def __str__(self):
        return str(self.id)


class Excepcion(models.Model):
    nombre = models.CharField(max_length=120)

    class Meta:
        unique_together = [['nombre',]]

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class ExcepcionCausa(models.Model):
    causa = models.ForeignKey(Causa, on_delete=models.CASCADE)
    excepcion = models.ForeignKey(Excepcion, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['causa', 'excepcion',]]

    def __str__(self):
        return str(self.id)
