from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Company(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class Jurisdiccion(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class Abogado(models.Model):
    nombre = models.CharField(max_length=120)
    correo = models.CharField(max_length=120, blank=True, null=True)
    telefono1 = models.CharField(max_length=20, blank=True, null=True)
    telefono2 = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class BonoJus(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class Excepcion(models.Model):
    nombre = models.CharField(max_length=120)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class TipoProceso(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class Oficio(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class EstadoProcesal(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class ObservacionPMP(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class EstadoNegociacion(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class ObservacionPericia(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class Causa(models.Model):
    fecha_derivacion = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    asunto = models.IntegerField()
    caratula = models.CharField(max_length=280)
    expediente = models.CharField(max_length=40)
    jurisdiccion = models.ForeignKey(Jurisdiccion, on_delete=models.CASCADE)
    tribunal = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])
    tipo_proceso = models.ForeignKey(TipoProceso, on_delete=models.CASCADE)
    fecha_inicio_demanda = models.DateField()
    incapacidad_reclamada = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    lesiones_reclamada = models.CharField(max_length=280, blank=True, null=True)
    reclama_dano_sicologico = models.BooleanField(default=False)
    monto_demanda = models.DecimalField(max_digits=14, decimal_places=2)
    fecha_pmi = models.DateField()
    porcentaje_srt = models.DecimalField(max_digits=5, decimal_places=2)
    abogado = models.ForeignKey(Abogado, on_delete=models.CASCADE)
    bono_y_jus = models.ForeignKey(BonoJus, on_delete=models.CASCADE)
    monto_jus = models.DecimalField(max_digits=14, decimal_places=2)
    monto_bono = models.DecimalField(max_digits=14, decimal_places=2)
    excepcion = models.ForeignKey(Excepcion, models.SET_NULL, blank=True, null=True)
    detalle = models.CharField(max_length=280, blank=True, null=True)
    preexistencia = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    estado_procesal = models.ForeignKey(EstadoProcesal, models.SET_NULL, blank=True, null=True)
    negociable_pmo = models.BooleanField(default=False)
    negociable_pmp = models.BooleanField(default=False)
    observacion_pericia = models.CharField(max_length=120, blank=True, null=True)
    fecha_pedido_pmp = models.DateField()
    fecha_asigno_pmp = models.DateField()
    fecha_pmp = models.DateField()
    porcentaje_pmp = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    monto_autorizado = models.DecimalField(max_digits=14, decimal_places=2)
    estado_negociacion = models.ForeignKey(EstadoNegociacion, on_delete=models.CASCADE)
    ofrecimiento = models.DecimalField(max_digits=14, decimal_places=2)
    contra_oferta = models.DecimalField(max_digits=14, decimal_places=2)
    fecha_ultimo_ofrecimiento = models.DateField()
    monto_acuerdo = models.DecimalField(max_digits=14, decimal_places=2)
    fecha_presentacion_acuerdo = models.DateField()
    hay_cbu = models.BooleanField(default=False)
    homologado = models.BooleanField(default=False)
    fecha_pedido_fondos = models.DateField()
    fecha_venci_pago = models.DateField()
    observacion = models.CharField(max_length=120, blank=True, null=True)
    ppmed = models.CharField(max_length=60, blank=True, null=True)
    ppsic = models.CharField(max_length=60, blank=True, null=True)
    pcont = models.CharField(max_length=60, blank=True, null=True)
    oficios = models.ForeignKey(Oficio, models.SET_NULL, blank=True, null=True)
    confesional = models.BooleanField(default=False)
    testimonial = models.BooleanField(default=False)
    otras_pruebas = models.CharField(max_length=60, blank=True, null=True)
    sentencia = models.CharField(max_length=60, blank=True, null=True)
    pedido_fondos = models.CharField(max_length=60, blank=True, null=True)
    fecha_facturado = models.DateField()

    def __str__(self):
        return self.company + ' ' + self.asunto + ' ' + self.caratula


class TipoVencimiento(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre


class Vencimiento(models.Model):
    fecha = models.DateField()
    causa = models.ForeignKey(Causa, on_delete=models.CASCADE)
    tipoVencimiento = models.ForeignKey(TipoVencimiento,
                                        on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha) + ' - ' + self.tipoVencimiento + ' - ' \
             + self.causa
