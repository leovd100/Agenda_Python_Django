from django.contrib import admin
from core.models import Evento
# Register your models here.
class EventoAdimin(admin.ModelAdmin):
	list_display = ('titulo','data_evento','data_criacao') # pega os campos do models.py e aprenseta na tela criando uma tabela
	list_filter = ('titulo','user',) # filtro, pode filtrar por titulo, usuário, data ...
admin.site.register(Evento,EventoAdimin)