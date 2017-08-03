from django.db import models
from fe_core.models import UUIDModel


class Endereco(UUIDModel):
    url = models.URLField()
    ativo = models.BooleanField(default=True)


class Verificacao(UUIDModel):
    OK_200 = 200
    NOT_FOUND_404 = 404
    CHOICES_STATUS = (
        (OK_200, 'OK'),
        (NOT_FOUND_404, 'NOT FOUND'),
    )
    endereco = models.ForeignKey(Endereco)
    status = models.IntegerField(choices=CHOICES_STATUS)
