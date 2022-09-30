import unittest

from django.test import TestCase, Client
from django.urls import reverse, resolve

from register.views import index


####################### Tests
# En las URL, comprobamos simplemente que el
# name esté asignado a la función.

# En las views, verificamos la respuesta http
# para el get y el post, y en cada uno verificamos
# el uso del template que se retorna.

class Test(TestCase):

    def general(self):
        self.client = Client()

    def test_index_url(self):
        url = reverse('index')
        
        self.assertEquals(resolve(url).func, index)
    
    def test_index_GET(self):
        r = self.client.get(reverse('index'))

        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed(r, 'index.html')

    def test_index_POST(self):
        r = self.client.post(reverse('index'))
        
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed(r, 'form_sent.html')
        
