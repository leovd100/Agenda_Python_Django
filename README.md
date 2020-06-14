## Agenda_Python_Django

#### Objetivo:
	Este projeto tem como objetivo criar uma agenda estilo to-do list com Python Django. 
	
	
	
![Screens](https://i.imgur.com/KDryu8r.png "Screens")
	
<hr style="height: 10px;">
##### Login
	Tela de login, com Admin, somente ele pode cadastrar novos usuários
	
![CSS e DJango](https://i.imgur.com/1tfRkoo.png "CSS e DJango")


### CSS no Django

Para trabalhar com CSS no Django, utilizamos a pasta "static" dentro da pasta Core do projeto.

![core](https://i.imgur.com/q36AdSw.png "core")

Adicionamos o STATICFILES_DIRS no arquivo settings 

![settings](https://i.imgur.com/pz138Yh.png "settings")

No HTML, adicionamos o {% load static %} em cima da tag < link> e no SRC adicionamos {"% static 'caminho' %"}


![load](https://i.imgur.com/cYw8Geq.png "load")

Lista de tarefas (Retificada)
![lista](https://i.imgur.com/mAHZp66.png "lista")

tela de cadastro de novo item da lista

![Cadastro de novo item](https://i.imgur.com/MWQxBG7.png "Cadastro de novo item")