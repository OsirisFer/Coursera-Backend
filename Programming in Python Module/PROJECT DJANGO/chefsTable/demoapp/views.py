from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.") 

from demoapp.forms import InputForm
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def form_view(request):
    form = InputForm()
    context = {'form': form}
    return render(request, 'home.html', context)

@api_view(['GET'])
def books(request):
    return Response({"message": "API funcionando"})