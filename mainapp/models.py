from django.db import models
from django.utils import timezone


class PendientesBajada(models.Model):
    id = models.TextField(primary_key=True)
    clave = models.TextField()
    tipo = models.TextField()
    autor = models.TextField()
    origen = models.TextField()
    timestamp = models.TextField()
    accion = models.TextField()


class RegistroPacienteCdb(models.Model):
    folio = models.TextField(primary_key=True)
    doctor = models.TextField()
    paciente = models.TextField()
    descuento = models.TextField()
    subtotal = models.TextField()
    total = models.TextField()
    fecha = models.TextField()
    hora = models.TextField()
    telefono = models.TextField()
    edad = models.IntegerField()
    meses = models.IntegerField()
    sv1 = models.TextField()
    qt1 = models.TextField()
    nt1 = models.TextField()
    pr1 = models.TextField()
    sv2 = models.TextField()
    qt2 = models.TextField()
    nt2 = models.TextField()
    pr2 = models.TextField()
    sv3 = models.TextField()
    qt3 = models.TextField()
    nt3 = models.TextField()
    pr3 = models.TextField()
    sv4 = models.TextField()
    qt4 = models.TextField()
    nt4 = models.TextField()
    pr4 = models.TextField()
    sv5 = models.TextField()
    qt5 = models.TextField()
    nt5 = models.TextField()
    pr5 = models.TextField()
    comision = models.IntegerField()
    id_doctor = models.TextField()
    tiempo_espera = models.TextField()
    folio = models.TextField(primary_key=True)
    tomas = models.TextField()


class DoctorCdb(models.Model):
    id = models.TextField(primary_key=True)
    doctor = models.TextField()
    comision = models.TextField()
    fecha_ult_liq = models.TextField()
    fecha_penult_liq = models.TextField()
    banco = models.TextField()
    numero_cuenta = models.TextField()
    propietario = models.TextField()
    mail = models.TextField()


class SucursalesCdb(models.Model):
    inventario = models.IntegerField()
    timestamp_bajada = models.DateTimeField()
    timestamp_subida = models.DateTimeField()
    prefijo = models.TextField()
    nombre = models.TextField()


class Historial(models.Model):
    id = models.TextField(primary_key=True)
    clave = models.TextField()
    tipo = models.TextField()
    autor = models.TextField()
    origen = models.TextField()
    timestamp = models.TextField()
    accion = models.TextField()
