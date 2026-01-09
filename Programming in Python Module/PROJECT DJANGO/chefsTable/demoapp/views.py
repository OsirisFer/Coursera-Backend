from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.") 

from demoapp.forms import InputForm

def form_view(request):
    form = InputForm()
    context = {'form': form}
    return render(request, 'home.html', context)
