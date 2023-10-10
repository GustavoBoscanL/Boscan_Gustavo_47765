from django.urls import path
from . import views
from CarWash_App.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    #HomePage
    path("", inicio, name="inicio"),

    #Usuarios
    path('login/', auth_views.LoginView.as_view(template_name='CarWash_App/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('hacer_reserva/', views.hacer_reserva, name='hacer_reserva'),
    #path('editar_precios/', views.editar_precios, name='editar_precios'),
    path('agregar_empleado/', views.agregar_empleado, name='agregar_empleado'),
    #Avatar
    path('crear_avatar/', views.crear_avatar, name='crear_avatar'),
    path('editar_avatar/', views.editar_avatar, name='editar_avatar'),

#Reservas
    path('ver_turnos_reservados/', ver_turnos_reservados, name='ver_turnos_reservados'),
    path('editar_reserva/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),

#Blog
    path('blog/', lista_publicaciones, name='lista_publicaciones'),
    


#Precios
    path('cotizar/', views.cotizacion, name="cotizar")


]

    
 
