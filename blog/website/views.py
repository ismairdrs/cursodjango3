from django.shortcuts import render
from prettytable import PrettyTable
from django.http import HttpResponse

def hello_blog(request):
    lista = [
        'Django', 'Python', 'git', 'html','css', 'banco de dado', 'linux', 'ngix']
    data = {'name': 'Curso de Django', 'lista_tec' : lista}
    return render(request, 'index.html', data)


