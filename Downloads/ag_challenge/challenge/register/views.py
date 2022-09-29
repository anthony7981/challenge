import random

from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Applicants

# Create your views here.

def index(request):
    """
    Comprobamos el método de la request. Luego,
    obtenemos todos los datos de un formulario 
    creado manualmente en HTML, los pasamos al
    modelo y verificamos que cumpla con los
    requisitos establecidos en models.py.

    Si los cumple, registramos al usuario y
    enviamos un mail de respuesta aleatoria. Si no
    (ValidationError), lo devolvemos a la vista
    con un mensaje de error.
    """
    if request.method == 'POST':

        try:
            applicant = Applicants(
                email = request.POST.get('email'),
                first_name = request.POST.get('name'),
                last_name = request.POST.get('last_name'),
                country = request.POST.get('country'),
                phone = request.POST.get('phone'),
                position = request.POST.get('position')
            )
            applicant.full_clean()
            applicant.save()
            
            number = random.randint(0,1)
            if number == 0:
                message = '¡Gracias por tu interés!\n\nTe agradecemos haber aplicado en nuestro proceso. Lamentablemente, no has sido elegido en el sorteo.\n\n¡Suerte la próxima!'
            else:
                message = '¡Buenas noticias!\n\nHas sido seleccionado en nuestro proceso'

            send_mail(
                subject='Unicornio de Latam',
                message=message,
                from_email='anthonygoncalvesg883@gmail.com',
                recipient_list=[applicant.email]
            )
            return render(request, 'form_sent.html', {"applicant": applicant})

        except ValidationError:
            return render(request, 'form_sent.html', {'title': "Ha habido un error", 'text': "Parece que los datos son inválidos o el usuario ya se encuentra registrado"})

    else:
        return render(request, 'index.html')

