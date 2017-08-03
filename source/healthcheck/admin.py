from django.contrib import admin

from healthcheck.models import Endereco, Verificacao


@admin.register(Endereco)
class EnderecoModelAdmin(admin.ModelAdmin):
    search_fields = ['url', ]
    list_filter = ['ativo', ]
    list_display = ['get_uuid', 'url', 'ativo']


@admin.register(Verificacao)
class VerificacaoModelAdmin(admin.ModelAdmin):
    search_fields = ['endereco', ]
    list_display = ['get_uuid', 'endereco', 'status']
