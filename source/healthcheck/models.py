import logging

import requests
from django.db import models
from fe_core.models import UUIDModel

log = logging.getLogger(__name__)


class Endereco(UUIDModel):
    url = models.URLField()
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = u'Endereço'
        verbose_name_plural = u'Endereços'
        ordering = ('url',)

    def __str__(self):
        return self.url

    def verificar(self):
        log.debug("Verificando URL={URL}".format(URL=self.url))
        r = requests.get(self.url)
        Verificacao.objects.create(
            endereco=self,
            status=r.status_code
        )


class Verificacao(UUIDModel):
    OK_200 = 200
    NOT_FOUND_404 = 404
    CHOICES_STATUS = (
        (OK_200, 'OK'),
        (NOT_FOUND_404, 'NOT FOUND'),
    )
    endereco = models.ForeignKey(Endereco)
    status = models.IntegerField(choices=CHOICES_STATUS)

    class Meta:
        verbose_name = u'Verificação'
        verbose_name_plural = u'Verificações'
        ordering = ('endereco',)

    def __str__(self):
        return '{ENDERECO} ({STATUS})'.format(ENDERECO=self.endereco, STATUS=self.status)
