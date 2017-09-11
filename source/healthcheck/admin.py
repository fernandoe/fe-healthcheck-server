from django.contrib import admin

from healthcheck.models import Endereco, Verificacao


@admin.register(Endereco)
class EnderecoModelAdmin(admin.ModelAdmin):
    search_fields = ['url', ]
    list_filter = ['ativo', ]
    list_display = ['get_uuid', 'url', 'ativo', 'get_last_status']

    def get_last_status(self, obj):
        verificoes = obj.verificacao_set.all().order_by('-created_at')
        if verificoes.count() == 0:
            return 'N/A'
        else:
            return verificoes[0].get_status_display()
    get_last_status.short_description = 'Last Status'



@admin.register(Verificacao)
class VerificacaoModelAdmin(admin.ModelAdmin):
    search_fields = ['endereco', ]
    list_display = ['get_uuid', 'endereco', 'created_at', 'status']
