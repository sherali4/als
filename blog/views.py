from django.shortcuts import render
from django.contrib.sites import requests
from django.http import HttpResponse
from .models import Company, Daraja, Profile
# Create your views here.

# def index(request):
#     # return HttpResponse('dasdasd asg djags jddhgasjdgh')
#     return render(request, template_name='blog/index.html')
def index(request):
    respublika = Company.objects.all().filter(turi=4, publish = 1)
    viloyat = Company.objects.all().filter(turi=7, publish = 1)
    contex = {
        'respublika':respublika,

        'viloyat': viloyat
    }
    return render(request, template_name='blog/index.html', context=contex)