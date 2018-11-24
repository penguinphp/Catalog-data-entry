from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from info.models import Mineral

def home(request):
    mineral_list = Mineral.objects.all()
    context = {
        'mineral_list': mineral_list,
    }
    return render(request, 'minerals/index.html', {'mineral_list': mineral_list})

def detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/detail.html', {'mineral': mineral})
