# challenge

Para poder desplegar este proyecto, primero debes usar virtualenv,
crear tu carpeta de entorno, volver a la ruta '/challenge' y ejecutar
este comando:

    pip install -r .\requirements.txt

Luego, debes dirigirte a la ruta donde has descargado el proyecto, 
abrir la carpeta 'challenge',abrir la consola y ejecutar el siguiente
comando:

    python manage.py makemigrations
    
Después:

    python manage.py migrate
  
Y finalmente:

    python manage.py runserver
    
# A TENER EN CUENTA

Dentro de la misma ruta, debes crear un archivo '.env' que contenga
las siguientes variables de entorno:
    
    EMAIL_HOST_USER=(tu correo electrónico)
    EMAIL_HOST_PASSWORD=(tu contraseña de acceso a terceros)
    SECRET_KEY=(tu secret key django)

También deberás cambiar las variables del 'settings.py' correspondientes
en caso de que uses otro host diferente de gmail.
