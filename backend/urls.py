from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [ #Urls para mostrar a views
    path('', home), 
    path('salvar/', salvar, name="salvar"), #O primeiro salvar/ seria a nova url que ele iria quando salvasse. o salvar normal seria o nome da função. e o name="salvar" seria um name de variável para no index.html no form, achar a url que está com o name de "salvar" igual eu coloquei lá, mas poderia ser qlqr outro
    path('editar/<int:id>', editar, name="editar"), #Aqui a mesma coisa, só que desta vez, estou indicando que no path, receberá editar/id um id que for passado pelo usuário
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete")
]
