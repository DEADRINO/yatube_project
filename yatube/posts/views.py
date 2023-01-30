from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('ГЛАВНАЯЯЯЯ СТРАНИЦАА')

def group_posts(request, slug):
    return HttpResponse('КРч вторая суета')