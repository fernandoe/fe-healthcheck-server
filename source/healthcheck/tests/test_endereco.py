from django.test import TestCase

from healthcheck.models import Endereco, Verificacao


class TestEndereco(TestCase):

    def test_verificar_ok(self):
        endereco = Endereco.objects.create(url='https://www.google.com')
        endereco.verificar()
        v = Verificacao.objects.last()
        self.assertEqual(1, Verificacao.objects.all().count())
        self.assertEqual(endereco, v.endereco)
        self.assertEqual(200, v.status)

    def test_verificar_404(self):
        endereco = Endereco.objects.create(url='https://www.fernandoe.com/not_found')
        endereco.verificar()
        v = Verificacao.objects.last()
        self.assertEqual(1, Verificacao.objects.all().count())
        self.assertEqual(endereco, v.endereco)
        self.assertEqual(404, v.status)
