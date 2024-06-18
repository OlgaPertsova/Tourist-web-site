from django.shortcuts import render
from .models import *


def cities(request):
    city = City.objects.all()
    context = {'cities': city}
    return render(request, 'cities/list_of_cities.html', context)


def city(request, pk):
    city_obj = City.objects.get(id=pk)
    excursions = city_obj.excursions_set.all()
    context = {
        'city': city_obj,
        'excursions': excursions
    }

    return render(request, 'cities/specific_city.html', context)

