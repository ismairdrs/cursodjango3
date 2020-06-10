from django.http import HttpResponse

from prettytable import PrettyTable

def hello_world(request):

    return HttpResponse("Hello")