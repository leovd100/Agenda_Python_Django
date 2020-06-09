"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import lista_eventos, login_user,submit_login, logout_user,evento_user, submit_evento,delete_evento,json_lista_evento
from django.views.generic import RedirectView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/',lista_eventos),
    path('agenda/evento/<int:id_usuario>',json_lista_evento),
    path('',RedirectView.as_view(url='/agenda/')),
    path('login/',login_user),
    path('login/submit',submit_login),
    path('logout/',logout_user),
    path('agenda/evento/',evento_user),
    path('agenda/evento/submit',submit_evento),
    path('agenda/evento/delete/<int:id_evento>', delete_evento)

] 

