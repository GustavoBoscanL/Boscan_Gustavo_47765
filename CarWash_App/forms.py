from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Reserva, Precio, Empleado
from django.forms import SelectDateWidget
import datetime


#Formulario de registro de usuario
class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'avatar']

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'avatar']

#Formulario de reserva
class ReservaForm(forms.ModelForm):
    fecha_reserva = forms.DateField(
        widget=forms.SelectDateWidget(),
        initial=datetime.date.today
    )
    turno = forms.TimeField(
        widget=forms.Select(choices=[(datetime.time(hour, minute), f'{hour:02d}:{minute:02d}') for hour in range(8, 20) for minute in [0, 30]]),
        initial=datetime.time(8, 0)
    )

    class Meta:
        model = Reserva
        fields = ['fecha_reserva', 'turno']

#Formulario de precios
class PrecioForm(forms.ModelForm):
    class Meta:
        model = Precio
        fields = ['tipo_auto', 'lavado_rapido', 'lavado_intenso']

#Formulario de empleados
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'cargo', 'especialidad', 'experiencia']