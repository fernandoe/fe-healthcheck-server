from django.core.management.base import BaseCommand

from healthcheck.models import Endereco


class Command(BaseCommand):
    def handle(self, *args, **options):
        enderecos = Endereco.objects.filter(ativo=True)
        for endereco in enderecos:
            endereco.verificar()
