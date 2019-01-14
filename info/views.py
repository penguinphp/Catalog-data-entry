from django.shortcuts import render, get_object_or_404

from info.models import Mineral
import string


groups = ['Silicates', 'Oxides', 'Sulfates', 'Carbonates', 'Halides',
          'Sulfosalts', 'Phosphates', 'Borates', 'Organic Minerals',
          'Arsenates', 'Native Elements', 'Other']

def home(request):
    mineral_list = Mineral.objects.all()
    context = {
        'mineral_list': mineral_list,
        'groups': groups,
        'group_name': None
    }
    return render(request, 'minerals/index.html', {'mineral_list': mineral_list})

def detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/detail.html', {'mineral': mineral})
<<<<<<< HEAD


def search_by_group(request, group_name):
    all_minerals = Mineral.objects.all()
    groups = {mineral.group for mineral in all_minerals}
    minerals = all_minerals.filter(group__icontains=group_name)
    return render(request, 'minerals/index.html',
                  {
                      'all_minerals': all_minerals,
                      'groups': groups,
                      'minerals': minerals,
                      'group_name': group_name
                  })




=======
>>>>>>> 9abb7a0e56ecbf12349adc4a5bf617d97e164dfe
