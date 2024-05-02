from django.shortcuts import render, redirect #Redirect para usar no update
from .models import *

def home(request):
    usuarios = Users.objects.all() #Pegando o Users do banco de dados e chamando todos 
    return render(request, "index.html", {"pessoas": usuarios}) #dentro da {"nome da variavel": valor} como um dicionário

def salvar(request):
    nNome = request.POST.get("nome") #Variável para pegar o nome do form e dar um post no banco
    nEmail = request.POST.get("email")
    Users.objects.create(nome=nNome, email=nEmail) #Linha que cria um novo usuário com nome igual do nome do forms
    usuarios = Users.objects.all() #Pegando novamente os usuários, para desta vez pegar o novo usuário que eu criei
    return render(request, "index.html", {"pessoas": usuarios}) #Retornando com os usuários novos

def editar(request, id):
    pessoa = Users.objects.get(id=id)
    return render(request, "update.html", {"pessoa": pessoa})

def update(request, id):
    nNome = request.POST.get("nome")
    nEmail = request.POST.get("email")
    pessoa = Users.objects.get(id=id)
    pessoa.nome, pessoa.email = nNome, nEmail
    pessoa.save()
    return redirect(home)

def delete(request, id):
    pessoa = Users.objects.get(id=id)
    pessoa.delete()
    return redirect(home)