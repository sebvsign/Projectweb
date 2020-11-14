from django.test import TestCase
from django.urls import reverse, resolve
from .models import Usuario
# Create your tests here.

class testUrls():

    def Test_detail_url(self):
        path = reverse('formulario', kwargs={'pk': 1})
        assert resolve(path).view_name == 'formulario'

