from django.contrib import admin
from .models import PendientesBajada, RegistroPacienteCdb, DoctorCdb, SucursalesCdb, Historial

admin.site.register(PendientesBajada)
admin.site.register(RegistroPacienteCdb)
admin.site.register(DoctorCdb)
admin.site.register(SucursalesCdb)
admin.site.register(Historial)
