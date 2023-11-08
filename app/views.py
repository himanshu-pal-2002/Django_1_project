from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Himanshu(request):
    return HttpResponse('<h1><marquee>Hello Himanshu How are you</h1></marquee>')
