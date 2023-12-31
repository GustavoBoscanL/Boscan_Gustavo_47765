# Boscan_Gustavo_47765

# Proyecto Autolavado SantOli

Este proyecto es la entrega final del curso y se trata de un sistema web para gestionar un autolavado llamado SantOli. Permite a los usuarios registrarse, reservar turnos, conocer tarifas, acceder a un blog con consejos automotrices, entre otras funcionalidades.

## Características Principales

- **Registro de Usuarios:** Permite a los usuarios crear cuentas para acceder a las funcionalidades del autolavado.

- **Reservas de Turnos:** Los usuarios pueden reservar turnos para el lavado de sus vehículos, facilitando la gestión del tiempo.

- **Cotización de Precios:** Ofrece una herramienta de cotización de precios para que los usuarios conozcan el costo estimado del lavado.

- **Blog de Consejos Automotrices:** Contiene un blog con consejos útiles para el mantenimiento de vehículos.

- **Gestión de Perfil y Avatar:** Los usuarios pueden personalizar sus perfiles, incluyendo la asignación de avatares.

- **Contacto con la Empresa:** Proporciona un formulario de contacto para que los usuarios se comuniquen con la empresa.


## Contenido

1. [Instalación](#instalación)
2. [Uso](#uso)
3. [Casos de Prueba](#casos-de-prueba)
4. [Video Demostrativo](#video-demostrativo)
5. [Agradecimientos](#agradecimientos)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Razarac92/Boscan_Gustavo_47765.git
   cd CarWash


Configura el entorno virtual e instala las dependencias:

``` 
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
.\venv\Scripts\activate   # Para Windows
pip install -r requirements.txt
```

Aplica las migraciones:
```
python manage.py migrate
```
Usa las siguientes credenciales para el usuario superuser:



*   Usuario: gussuperusuario
*   Contraseña: Andres220714

Inicia el servidor:


```
python manage.py runserver
```
Visita http://localhost:8000 en tu navegador.

## Uso



1.   Inicia sesión con el superusuario proporcionado.
2.   Explora las diferentes funcionalidades del autolavado.


## Casos de Prueba

Se han creado casos de prueba para asegurar el correcto funcionamiento del sistema. Puedes encontrarlos en el archivo [Test_Cases_CarWash_App](https://docs.google.com/spreadsheets/d/1jigMG4uNQeTN9UbeK91gcYQPA-Ux4LCAVNipOYMNFFE/edit?usp=sharing)


## Video Demostrativo

Mira el video demostrativo para obtener una visión completa de cómo utilizar el sistema. [Video demostrativo](https://drive.google.com/file/d/1mpRXd5vOY9h0C7saW5ke7mQQQBe1zKxK/view?usp=sharing)


## Estado del Proyecto

Este proyecto está en desarrollo activo y se están realizando mejoras continuas. ¡Esperamos tus contribuciones y comentarios!


## Agradecimientos

Quiero agradecer a CoderHouse por su apoyo y a todos los contribuyentes que han ayudado a mejorar este proyecto, en especial al Profesor Juan Carlos Paredes que estuvo a cargo de la comisión y a mi tutor Ignacio Muñoz que fue clave para que este proyecto fuese realizado con éxtio.
