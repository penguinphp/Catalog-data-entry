from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from info.models import Mineral

groups = ['Silicates', 'Oxides', 'Sulfates', 'Carbonates', 'Halides',
          'Sulfosalts', 'Phosphates', 'Borates', 'Organic Minerals',
          'Arsenates', 'Native Elements', 'Sulfides', 'Other']

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']


def home(request):
    mineral_list = Mineral.objects.all()
    groups = {mineral.group for mineral in mineral_list}
    context = {
        'mineral_list': mineral_list,
        'groups': groups,
        'group_name': None,
        'alphabet': alphabet,
    }
    return render(request, 'minerals/index.html', context)


def detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/detail.html',
                  {
                      'mineral': mineral,
                      'groups': groups,
                      'alphabet': alphabet,
                  })



def search_by_group(request, group_name):
    all_minerals = Mineral.objects.all()
    groups = {mineral.group for mineral in all_minerals}
    minerals = all_minerals.filter(group__icontains=group_name)
    print("GROUPS: ", groups)
    return render(request, 'minerals/groups.html',
                  {
                      'all_minerals': all_minerals,
                      'groups': groups,
                      'minerals': minerals,
                      'group_name': group_name,
                      'alphabet': alphabet,
                  })


def search_by_letter(request, letter=None):
    all_minerals = Mineral.objects.all()
    minerals = all_minerals.filter(name__istartswith=letter)
    return render(request, 'minerals/letter.html',
                  {
                      'all_minerals': all_minerals,
                      'groups': groups,
                      'alphabet': alphabet,
                      'letter': letter,
                      'minerals': minerals,
                  })


def search_by_keyword(request):
    query = request.GET.get('q', '')
    all_minerals = Mineral.objects.all()
    minerals = all_minerals.filter(
        Q(name__icontains=query))
    return render(request, 'minerals/search.html', {
        'all_minerals': all_minerals,
        'groups': groups,
        'alphabet': alphabet,
        'minerals': minerals
    })
