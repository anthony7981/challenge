import email
from enum import unique
from random import choices
from django.db import models

# Create your models here.


############## APPLICANTS
#No establecemos la obligatoriedad de todos los
#campos puesto que ya lo hemos hecho desde el
#'index.html'. No trabajamos con 'forms.py' ni
#'ModelForm'.

#Establecemos el campo 'phone' como CharField
#dado que recibimos datos de varios países y
#podríamos recibir códigos de área.
class Applicants(models.Model):
    COUNTRIES = (
        ("Argentina", "Argentina"),
        ("Bolivia", "Bolivia"),
        ("Brasil", "Brasil"),
        ("Chile", "Chile"),
        ("Colombia", "Colombia"),
        ("Ecuador", "Ecuador"),
        ("Paraguay", "Paraguay"),
        ("Perú", "Perú"),
        ("Uruguay", "Uruguay"),
        ("Venezuela", "Venezuela")
    )

    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    country = models.CharField(max_length=9, choices=COUNTRIES)
    phone = models.CharField(max_length=30)
    position = models.CharField(max_length=128)

    def __str__(self):
        return self.first_name
    
