from django.shortcuts import render , HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1 style="padding-top:50px; margin-left:100px">Hello World {} de {} anos</h1>' .format(nome, idade))