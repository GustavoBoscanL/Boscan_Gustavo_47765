from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Reserva, Precio, Empleado, Avatar
from django.forms import SelectDateWidget
import datetime
from django.contrib.auth.models import User

#Formulario de registro de usuario
class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Requerido. Máximo 30 caracteres.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Requerido. Máximo 30 caracteres.')
    email = forms.EmailField(max_length=254, required=True, help_text='Requerido. Ingrese una dirección de correo válida.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está en uso. Por favor, elige otro.')
        return email

class EditarPerfilForm(UserChangeForm):
    password = forms.CharField(
        label='Contraseña',
        strip=False,
        widget=forms.PasswordInput,
        required=False  # No es requerido para la edición
    )

    new_password1 = forms.CharField(
        label='Nueva Contraseña',
        strip=False,
        widget=forms.PasswordInput,
        required=False  # No es requerido para la edición
    )

    new_password2 = forms.CharField(
        label='Confirmar Nueva Contraseña',
        strip=False,
        widget=forms.PasswordInput,
        required=False  # No es requerido para la edición
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Este correo electrónico ya está en uso. Por favor, elige otro.')
        return email

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['avatar']

class AvatarFormEditar(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['avatar']

    def __init__(self, *args, **kwargs):
        super(AvatarFormEditar, self).__init__(*args, **kwargs)
        # Personaliza las etiquetas y ayuda del formulario si es necesario
        self.fields['avatar'].label = 'Cambiar avatar'
        self.fields['avatar'].help_text = 'Seleccione una imagen para actualizar su avatar.'





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