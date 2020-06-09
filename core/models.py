from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
# Create your models here.


class Evento(models.Model):
	titulo = models.CharField(max_length=100,verbose_name='Evento')
	descricao =  models.TextField(blank=True,null=True)
	data_evento = models.DateTimeField(verbose_name='Data do evento')
	data_criacao = models.DateTimeField(auto_now=True,verbose_name='Data de criação do evento')
	user = models.ForeignKey(User, on_delete=models.CASCADE) # exclui tudo do usuário, efeito cascata exclui tudo junto
	local = models.CharField(max_length=100,null=True,verbose_name='Local do evento')
	class Meta:
		db_table = 'evento' 


	def __str__(self):
		return self.titulo # troca o nome do evento de objeto para o Título digitado


	def getDataEvento(self):
		return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')
	
	def get_data_input_evento(self):
		return self.data_evento.strftime('%Y-%m-%dT%H:%M')

	def evento_atrasado(self):
		if self.data_evento < datetime.now():
			return True
		else:
			return False