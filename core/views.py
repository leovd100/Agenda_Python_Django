from django.shortcuts import render,redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
# Create your views here.


@login_required(login_url='/login/')
def lista_eventos(request):
	user = request.user
	evento = Evento.objects.filter(user=user)
	dados = {'eventos': evento}


	return render(request,'agenda.html',dados)

def login_user(request):
	return render(request,'login.html')

def submit_login(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		usuario = authenticate(username=username, password=password)
		if usuario is not None:
			login(request, usuario)
			return redirect('/')
		else:
			messages.error(request,"Usuário ou senha inválidos.")
			#return redirect('/')

	#else:
	return	redirect('/')

def logout_user(request):
	logout(request)
	return redirect('/')


@login_required(login_url='/login/')
def evento_user(request):
	id_evento = request.GET.get('id')
	dados = {}
	if id_evento:
		dados['evento'] = Evento.objects.get(id=id_evento)

	return render(request,'evento.html',dados)

@login_required(login_url='/login/')
def submit_evento(request):
	if request.POST:
		titulo = request.POST.get('titulo') # recebe o titulo do name titulo do input do html 
		data_evento = request.POST.get('data_evento')
		descricao = request.POST.get('descricao')
		user = request.user # recebe o usuário
		local = request.POST.get('local')
		id_evento = request.POST.get('id_evento')
		if id_evento: #ATUALIZA
			Evento.objects.filter(id=id_evento).update(titulo=titulo,  
							data_evento=data_evento, 
								descricao=descricao,
								local=local,
								user=user)
		else: # CRIA
			Evento.objects.create(titulo=titulo,  # insere titulo no banco de dados no campo título
							data_evento=data_evento, # insere data_evento no banco de dados no campo data_evento
								descricao=descricao,
								local=local, # insere descricao no banco de dados o  no campo descicao
								user=user)  # insere usuario no banco de dados no campo user
	return redirect('/')





@login_required(login_url='/login/')
def delete_evento(request,id_evento):
	usuario = request.user
	evento = Evento.objects.get(id=id_evento)
	if usuario == evento.user:
		evento.delete()
	return redirect('/')
# def index(request):
# 	return redirect('/agenda/')