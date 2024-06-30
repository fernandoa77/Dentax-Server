from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import RegistroPacienteCdb, DoctorCdb, PendientesBajada, Historial, SucursalesCdb
from .forms import RegistroPacienteForm, DoctorForm
import uuid


def generate_custom_id():
    return str(uuid.uuid4())


def get_current_timestamp():
    return timezone.now().strftime('%Y-%m-%d %H:%M:%S')


def create_history_and_pendientes(instance, action, user):
    common_data = {
        'id': generate_custom_id(),
        'autor': user.username,
        'origen': 'C',
        'timestamp': get_current_timestamp(),
        'accion': action
    }

    if isinstance(instance, DoctorCdb):
        common_data['clave'] = instance.id
        common_data['tipo'] = 'DOCTOR'
    elif isinstance(instance, RegistroPacienteCdb):
        common_data['clave'] = instance.folio
        common_data['tipo'] = 'REGISTRO'

    # Insert into both PendientesBajada and Historial tables
    PendientesBajada.objects.create(**common_data)
    Historial.objects.create(**common_data)




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

#BASE VIEWS


#dash board views
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

#sucursales views
@login_required
def sucursales(request):
    return render(request, 'sucursales.html')

#comparar views?
@login_required
def comparar(request):
    return render(request, 'comparar.html')

#registros views
@login_required
def registros(request):
    registros_pacientes = RegistroPacienteCdb.objects.all()
    return render(request, 'registros/registros.html', {'registros_pacientes': registros_pacientes})

@login_required
def agregar_registro(request):
    if request.method == 'POST':
        form = RegistroPacienteForm(request.POST)
        if form.is_valid():
            registro = form.save()
            create_history_and_pendientes(registro, 'AGREGAR', request.user)
            return redirect('registros')
    else:
        form = RegistroPacienteForm()
    return render(request, 'agregar_registro.html', {'form': form})


@login_required
def editar_registro(request, folio):
    registro = get_object_or_404(RegistroPacienteCdb, folio=folio)
    if request.method == 'POST':
        form = RegistroPacienteForm(request.POST, instance=registro)
        if form.is_valid():
            registro = form.save()
            create_history_and_pendientes(registro, 'EDITAR', request.user)
            return redirect('registros')
    else:
        form = RegistroPacienteForm(instance=registro)
    return render(request, 'editar_registro.html', {'form': form})


@login_required
def eliminar_registro(request, folio):
    registro = get_object_or_404(RegistroPacienteCdb, folio=folio)
    if request.method == 'POST':
        create_history_and_pendientes(registro, 'ELIMINAR', request.user)
        registro.delete()
        return redirect('registros')
    return render(request, 'eliminar_registro.html', {'registro': registro})


#doctores views
@login_required
def doctores(request):
    doctores_list = DoctorCdb.objects.all()
    return render(request, 'doctores/doctores.html', {'doctores_list': doctores_list})

@login_required
def agregar_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save()
            create_history_and_pendientes(doctor, 'AGREGAR', request.user)
            return redirect('doctores')
    else:
        form = DoctorForm()
    return render(request, 'doctores/agregar_doctor.html', {'form': form})


@login_required
def editar_doctor(request, id):
    doctor = get_object_or_404(DoctorCdb, id=id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            doctor = form.save()
            create_history_and_pendientes(doctor, 'EDITAR', request.user)
            return redirect('doctores')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctores/editar_doctor.html', {'form': form})


@login_required
def eliminar_doctor(request, id):
    doctor = get_object_or_404(DoctorCdb, id=id)
    if request.method == 'POST':
        create_history_and_pendientes(doctor, 'ELIMINAR', request.user)
        doctor.delete()
        return redirect('doctores')
    return render(request, 'doctores/eliminar_doctor.html', {'doctor': doctor})



#admin views
@login_required
def pendientes_bajada(request):
    
    pendientes_records = PendientesBajada.objects.all()
    pendientes_columns = ['id', 'clave', 'tipo', 'autor', 'origen', 'timestamp', 'accion']
    context = {
        'pendientes_records': pendientes_records,
        'pendientes_columns': pendientes_columns
    }
    return render(request, 'admin/pendientes_bajada.html', context)


@login_required
def historial(request):
    historial_records = Historial.objects.all()
    historial_columns = ['id', 'clave', 'tipo', 'autor', 'origen', 'timestamp', 'accion']
    context = {
        'historial_records': historial_records,
        'historial_columns': historial_columns
    }
    return render(request, 'admin/historial.html', context)


@login_required
def sucursales_admin(request):
    sucursales_records = SucursalesCdb.objects.all()
    sucursales_columns = ['id', 'inventario', 'timestamp_bajada', 'timestamp_subida', 'prefijo', 'nombre']
    context = {
        'sucursales_records': sucursales_records,
        'sucursales_columns': sucursales_columns
    }
    return render(request, 'admin/sucursales_admin.html', context)
