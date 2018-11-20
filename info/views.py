from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from info.models import Mineral

def index(request):
    return HttpResponse("<h1>This is the minerals page</h1>")

def home(request):
    mineral_list = Mineral.objects.all()
    context = {
        'mineral_list': mineral_list,
    }
    return render(request, 'minerals/index.html', {'mineral_list': mineral_list})



