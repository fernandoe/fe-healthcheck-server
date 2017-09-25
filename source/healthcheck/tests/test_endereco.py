import requests_mock
from django.test import TestCase

from healthcheck.models import Endereco, Verificacao


class TestEndereco(TestCase):
    @requests_mock.Mocker()
    def test_verificar_ok(self, r_mock):
        url = 'https://www.google.com'
        r_mock.get(url, status_code=200)
        endereco = Endereco.objects.create(url=url)
        endereco.verificar()
        v = Verificacao.objects.last()
        self.assertEqual(1, Verificacao.objects.all().count())
        self.assertEqual(endereco, v.endereco)
        self.assertEqual(200, v.status)

    @requests_mock.Mocker()
    def test_verificar_404(self, r_mock):
        url = 'https://www.fernandoe.com/not_found'
        r_mock.get(url, status_code=404)
        endereco = Endereco.objects.create(url=url)
        endereco.verificar()
        v = Verificacao.objects.last()
        self.assertEqual(1, Verificacao.objects.all().count())
        self.assertEqual(endereco, v.endereco)
        self.assertEqual(404, v.status)
