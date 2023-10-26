# -*- coding: utf-8 -*-
__author__ = "Andrés Galaz"
__license__ = "LGPL"
__email__ = "andres.galaz@gmail.com"
__version__ = "v1.0"

import csv
import re
# import uuid
from datetime import datetime
from django.core.management import BaseCommand
from django.utils import timezone
from django.db.utils import DataError
from django.db import transaction
from legales.models import Company, Jurisdiccion, TipoProceso, Abogado, BonoJus, Excepcion, \
                           EstadoProcesal, EstadoNegociacion, Oficio, Causa


def str2date(cFecha):
    try:
        cFecha = cFecha.replace(".", "-").replace("/", "-")
        if re.search(
                "^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])" +
                "(\\.|-|/)([1-9]|0[1-9]|1[0-2])(\\.|-|/)" +
                "([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$",
                cFecha):
            return datetime.strptime(cFecha, '%d-%m-%Y').date()
        elif re.search(
                "^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])" +
                "(\\.|-|/)([1-9]|0[1-9]|1[0-2])(\\.|-|/)" +
                "([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$",
                cFecha):
            return datetime.strptime(cFecha, '%Y-%m-%d').date()
    except Exception:
        pass


def str2boolean(cBol):
    cBol = cBol.strip().upper()
    if cBol == 'S' or cBol == 'SI' or cBol == 'T' or cBol == 'TRUE' or cBol == '1':
        return True
    if cBol == 'N' or cBol == 'NO' or cBol == 'F' or cBol == 'FALSE' or cBol == '0':
        return False
    return None


def str2number(cNum):
    cNum = cNum.strip().replace(".", "").replace("\xa0%", "")
    try:
        if cNum.find(',') >= 0:
            cNum = cNum.replace(",", ".")
            return float(cNum)
        return int(cNum)
    except Exception:
        return None


def isRowEmpty(row):
    for r in row:
        if r.strip() != '':
            return False
    return True


class Command(BaseCommand):
    help = "Carga datos desde un archivo CSV."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    @transaction.atomic()
    def handle(self, *args, **options):
        start_time = timezone.now()
        file_path = options["file_path"]
        nLinea = 1
        nError = 0

        # encoding = 'cp437'
        with open(file_path, "r", encoding='utf8') as csv_file:
            data = list(csv.reader(csv_file, delimiter=";"))
            # Valida. Si hay errores no procesa nada
            for nPasada in range(0, 2, 1):
                print('Pasada:', nPasada)
                nLinea = 1
                for row in data:  # data[1:]:
                    nLinea += 1
                    if isRowEmpty(row):
                        continue

                    # 0 mes/año de derivacion;
                    csvFechaDerivacion = row[1].strip()  # DERIVACION;
                    csvCompany = row[2].strip()  # COMPAÑÍA;
                    csvAsunto = row[3].strip()  # ASUNTO;
                    csvCaratula = row[4].strip()  # CARATULA;
                    csvExpediente = row[5].strip()  # EXPEDIENTE;
                    csvJurisdiccion = row[6].strip()  # JURISDICCION;
                    csvTribunal = row[7].strip()  # NRO. TRIBUNAL;
                    csvTipoProceso = row[8].strip()  # TIPO DE PROCESO;
                    csvFechaInicioDemanda = row[9].strip()  # INICIO DEMANDA;
                    csvIncapacidadReclamada = row[10].strip()  # INCAPACIDAD RECLAMADA;
                    csvLesionesReclamada = row[11].strip()  # LESIONES RECLAMADAS;
                    csvReclamaDanoSicologico = row[12].strip()  # RECLAMA DAÑO PSICOLOGICO;
                    csvMontoDemanda = row[13].strip()  # MONTO DEMANDA;
                    csvFechaPmi = row[14].strip()  # FECHA PMI;
                    csvPorcentajeSrt = row[15].strip()  # % SRT;
                    csvAbogado = row[16].strip()  # ABOGADO LPA;
                    csvBonoYJus = row[17].strip()  # BONO Y JUS;
                    csvMontoJus = row[18].strip()  # JUS;
                    csvMontoBono = row[19].strip()  # BONO;
                    csvExcepcion = row[20].strip()  # EXCEPCIONES;
                    csvDetalle = row[21].strip()  # DETALLE;
                    csvPreexistencia = row[22].strip()  # PREEXISTENCIA;
                    csvEstadoProcesal = row[23].strip()  # ESTADO PROCESAL;
                    csvNegociablePmo = row[24].strip()  # NEGOCIABLE PMO;
                    csvNegociablePmp = row[25].strip()  # NEGOCIABLE PMP;
                    csvObservacionPericia = row[25].strip()  # OBSERVACIONES PERICIA;
                    csvFechaPedidoPmp = row[27].strip()  # PEDI PMP;
                    csvFechaAsignoPmp = row[28].strip()  # SE ASIGNO PMP;
                    csvFechaPmp = row[29].strip()  # FECHA PMP;
                    csvPorcentajePmp = row[30].strip()  # % PMP;
                    csvMontoAutorizado = row[31].strip()  # MONTO AUTORIZADO;
                    csvEstadoNegociacion = row[32].strip()  # ESTADO NEGOCIACION;
                    csvOfrecimiento = row[33].strip()  # OFRECIMIENTO;
                    csvContraOferta = row[34].strip()  # CONTRA OFERTA;
                    csvFechaUltimoOfrecimiento = row[35].strip()  # FECHA ULTIMO OFRECIMIENTO;
                    csvMontoAcuerdo = row[36].strip()  # MONTO ACUERDO;
                    csvFechaPresentacionAcuerdo = row[37].strip()  # PRESENTACION ACUERDO;
                    csvHayCbu = row[38].strip()  # HAY CBU;
                    csvHomologado = row[39].strip()  # HOMOLOGADO;
                    csvFechaPedidoFondos = row[40].strip()  # PEDIDO DE FONDOS;
                    csvFechaVenciPago = row[41].strip()  # VENCIMIENTO PAGO;
                    csvObservacion = row[42].strip()  # OBSERVACIONES;
                    csvPpmed = row[43].strip()  # PPMED;
                    csvPpsic = row[44].strip()  # PPSIC;
                    csvPcont = row[45].strip()  # PCONT;
                    csvOficios = row[46].strip()  # OFICIOS;
                    csvConfesional = row[47].strip()  # CONFESIONAL;
                    csvTestimonial = row[48].strip()  # TESTIMONIAL;
                    csvOtrasPruebas = row[49].strip()  # OTRAS PRUEBAS;
                    csvSentencia = row[50].strip()  # SENTENCIA;
                    csvPedidoFondos = row[51].strip()  # PEDIDO DE FONDOS;
                    csvFechaFacturado = row[52].strip()  # FACTURADO;
                    # 53 dias entre derivacion y pedido de PMP;
                    # 54 dias entre pedido y asignacion de PMP;
                    # 55 dias entre  asignacion y realizacion de pmp;
                    # 56 Diferencia entre acuerdo y monto demandado;
                    # 57 Tiene PMP?;
                    # 58 Ahorro en % incapacidad;

                    fechaDerivacion = str2date(csvFechaDerivacion)
                    try:
                        company = Company.objects.all().get(nombre=csvCompany)
                    except Exception:
                        nError += 1
                        print(nLinea, "No existe Company:"+csvCompany)
                    asunto = csvAsunto
                    caratula = csvCaratula
                    expediente = csvExpediente
                    try:
                        jurisdiccion = Jurisdiccion.objects.all().get(nombre=csvJurisdiccion)
                    except Exception:
                        nError += 1
                        print(nLinea, "No existe Jurisdiccion:"+csvJurisdiccion)
                    tribunal = str2number(csvTribunal)
                    try:
                        tipoProceso = TipoProceso.objects.all().get(nombre=csvTipoProceso)
                    except Exception:
                        tipoProceso = None
                        if csvTipoProceso != '':
                            nError += 1
                            print(nLinea, "No existe Tipo de Proceso:"+csvTipoProceso)
                    fechaInicioDemanda = str2date(csvFechaInicioDemanda)
                    incapacidadReclamada = str2number(csvIncapacidadReclamada)
                    lesionesReclamada = csvLesionesReclamada
                    reclamaDanoSicologico = str2boolean(csvReclamaDanoSicologico)
                    montoDemanda = str2number(csvMontoDemanda)
                    fechaPmi = str2date(csvFechaPmi)
                    porcentajeSrt = str2number(csvPorcentajeSrt)
                    try:
                        abogado = Abogado.objects.all().get(nombre=csvAbogado)
                    except Exception:
                        if csvAbogado != '':
                            nError += 1
                            print(nLinea, "No existe abogado:"+csvAbogado)
                    try:
                        bonoJus = BonoJus.objects.all().get(nombre=csvBonoYJus)
                    except Exception:
                        if csvBonoYJus != '':
                            nError += 1
                            print(nLinea, "No existe Bono y Jus:"+csvBonoYJus)
                    montoJus = str2number(csvMontoJus)
                    montoBono = str2number(csvMontoBono)
                    excepcion = None if csvExcepcion == '' else Excepcion.objects.all().get(nombre=csvExcepcion)
                    detalle = csvDetalle
                    preexistencia = str2number(csvPreexistencia)
                    estadoProcesal = str2number(csvEstadoProcesal)
                    negociablePmo = str2boolean(csvNegociablePmo)
                    negociablePmp = str2boolean(csvNegociablePmp)
                    try:
                        estadoProcesal = EstadoProcesal.objects.all().get(nombre=csvEstadoProcesal)
                    except Exception:
                        if csvEstadoProcesal != '':
                            nError += 1
                            print(nLinea, "No existe Estado Procesal:"+csvEstadoProcesal)
                    observacionPericia = csvObservacionPericia
                    fechaPedidoPmp = str2date(csvFechaPedidoPmp)
                    fechaAsignoPmp = str2date(csvFechaAsignoPmp)
                    fechaPmp = str2date(csvFechaPmp)
                    porcentajePmp = str2number(csvPorcentajePmp)
                    montoAutorizado = str2number(csvMontoAutorizado)
                    estadoNegociacion = None if csvEstadoNegociacion == '' else EstadoNegociacion.objects.all().get(nombre=csvEstadoNegociacion)
                    ofrecimiento = str2number(csvOfrecimiento)
                    contraOferta = str2number(csvContraOferta)
                    fechaUltimoOfrecimiento = str2date(csvFechaUltimoOfrecimiento)
                    montoAcuerdo = str2number(csvMontoAcuerdo)
                    fechaPresentacionAcuerdo = str2date(csvFechaPresentacionAcuerdo)
                    hayCbu = str2boolean(csvHayCbu)
                    homologado = str2boolean(csvHomologado)
                    fechaPedidoFondos = str2boolean(csvFechaPedidoFondos)
                    fechaVenciPago = str2date(csvFechaVenciPago)
                    observacion = csvObservacion
                    ppmed = csvPpmed
                    ppsic = csvPpsic
                    pcont = csvPcont
                    oficios = None if csvOficios == '' else Oficio.objects.all().get(nombre=csvOficios)
                    confesional = str2boolean(csvConfesional)
                    testimonial = str2boolean(csvTestimonial)
                    otrasPruebas = csvOtrasPruebas
                    sentencia = csvSentencia
                    pedidoFondos = csvPedidoFondos
                    fechaFacturado = str2date(csvFechaFacturado)
                    # Si es la pasada 1, ya está validado y no hay errores, asi es que se procesa

                    # if nLinea % 100 == 0:
                    #     print('Procesando [', nPasada, ']:', nLinea)
                    if nPasada == 0:
                        continue

                    try:
                        causa = Causa.objects.create(
                            fecha_derivacion=fechaDerivacion,
                            company=company,
                            asunto=asunto,
                            caratula=caratula,
                            expediente=expediente,
                            jurisdiccion=jurisdiccion,
                            tribunal=tribunal,
                            tipo_proceso=tipoProceso,
                            fecha_inicio_demanda=fechaInicioDemanda,
                            incapacidad_reclamada=incapacidadReclamada,
                            lesiones_reclamada=lesionesReclamada,
                            reclama_dano_sicologico=reclamaDanoSicologico,
                            monto_demanda=montoDemanda,
                            fecha_pmi=fechaPmi,
                            porcentaje_srt=porcentajeSrt,
                            abogado=abogado,
                            bono_y_jus=bonoJus,
                            monto_jus=montoJus,
                            monto_bono=montoBono,
                            excepcion=excepcion,
                            detalle=detalle,
                            preexistencia=preexistencia,
                            estado_procesal=estadoProcesal,
                            negociable_pmo=negociablePmo,
                            negociable_pmp=negociablePmp,
                            observacion_pericia=observacionPericia,
                            fecha_pedido_pmp=fechaPedidoPmp,
                            fecha_asigno_pmp=fechaAsignoPmp,
                            fecha_pmp=fechaPmp,
                            porcentaje_pmp=porcentajePmp,
                            monto_autorizado=montoAutorizado,
                            estado_negociacion=estadoNegociacion,
                            ofrecimiento=ofrecimiento,
                            contra_oferta=contraOferta,
                            fecha_ultimo_ofrecimiento=fechaUltimoOfrecimiento,
                            monto_acuerdo=montoAcuerdo,
                            fecha_presentacion_acuerdo=fechaPresentacionAcuerdo,
                            hay_cbu=hayCbu,
                            homologado=homologado,
                            fecha_pedido_fondos=fechaPedidoFondos,
                            fecha_venci_pago=fechaVenciPago,
                            observacion=observacion,
                            ppmed=ppmed,
                            ppsic=ppsic,
                            pcont=pcont,
                            oficios=oficios,
                            confesional=confesional,
                            testimonial=testimonial,
                            otras_pruebas=otrasPruebas,
                            sentencia=sentencia,
                            pedido_fondos=pedidoFondos,
                            fecha_facturado=fechaFacturado
                            )
                        print(causa)

                    except DataError as e:
                        transaction.set_rollback(True)
                        print(nLinea, 'Error SQL:', e, row)
                        exit(-1)

                if nError > 0:
                    break

        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(f"""
========================================================================
La carga CSV tomó: {(end_time-start_time).total_seconds()} segundos.
Lineas procesadas {nLinea}
Errores encontrados {nError}
========================================================================
"""))
