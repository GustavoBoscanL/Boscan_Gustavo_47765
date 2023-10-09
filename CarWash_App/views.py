from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from .models import *


def inicio(request): #home page
    return render(request, "CarWash_App/inicio.html")

#Usuarios
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = RegistroForm()

    return render(request, 'CarWash_App/registro.html',{'form':form})


@login_required
def perfil(request):
    return render(request, 'CarWash_App/perfil.html')

@login_required
def editar_perfil(request):
 if request.method == 'POST':
     form = EditarPerfilForm(request.POST, instance=request.user)
     if form.is_valid():
         form.save()
         return redirect('perfil')  # Puedes cambiar la URL a la que desees redirigir después de editar el usuario
 else:
     form = EditarPerfilForm(instance=request.user)

 return render(request, 'CarWash_App/editar_perfil.html', {'form': form})

@login_required
def crear_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar_anterior = Avatar.objects.filter(user=request.user)
            if (len(avatar_anterior) > 0):
                avatar_anterior.delete()
            avatar_nuevo = Avatar(
                user=request.user, avatar=form.cleaned_data["avatar"])
            avatar_nuevo.save()
            return redirect('perfil')
    else:
        form = AvatarForm()

    return render(request, 'CarWash_App/crear_avatar.html',{'form':form})

@login_required
def editar_avatar(request):
 try:
     avatar = Avatar.objects.get(user=request.user)
 except Avatar.DoesNotExist:
     avatar = None

 if request.method == 'POST':
     form = AvatarFormEditar(request.POST, request.FILES, instance=avatar)
     if form.is_valid():
         avatar = form.save(commit=False)
         avatar.user = request.user  # Asigna el usuario al avatar
         avatar.save()
         return redirect('perfil')  # Puedes cambiar la URL a la que desees redirigir después de editar el avatar
 else:
     form = AvatarFormEditar(instance=avatar)

 return render(request, 'CarWash_App/editar_avatar.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('inicio')  



#Reservas
@login_required
def hacer_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            return redirect('ver_turnos_reservados')  # Redirige a la vista de turnos reservados
    else:
        form = ReservaForm()

    return render(request, 'CarWash_App/hacer_reserva.html', {'form': form})

@login_required
def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id, usuario=request.user)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'edit':
            form = ReservaForm(request.POST, instance=reserva)
            if form.is_valid():
                form.save()
                return redirect('ver_turnos_reservados')
        elif action == 'delete':
            reserva.delete()
            return redirect('ver_turnos_reservados')
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'CarWash_App/editar_reserva.html', {'form': form, 'reserva': reserva})



@login_required
def ver_turnos_reservados(request):
    # Obtener todas las reservas del usuario actual
    reservas = Reserva.objects.filter(usuario=request.user)
    
    return render(request, 'CarWash_App/ver_turnos_reservados.html', {'reservas': reservas})



#Precios
def editar_precios(request):
    if request.method == 'POST':
        form = PrecioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = PrecioForm()
    return render(request, 'CarWash_App/editar_precios.html', {'form': form})

#Empleados
def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EmpleadoForm()
    return render(request, 'CarWash_App/agregar_empleado.html', {'form': form})