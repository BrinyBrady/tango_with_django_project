from django.shortcuts import render

from django.http import HttpResponse

def index (request):
    return HttpResponse("why did u play chunriying?")
