from django.shortcuts import render, redirect
from cities.models import City
from directions.models import Tours
from events.models import Festival
import datetime


def index(request):
    city = City.objects.exclude(preview=None)
    tours = Tours.objects.filter(rating__range=(4, 5))
    today = datetime.date.today()
    events = Festival.objects.filter(date_of_the__month=str(today.month))
    context = {'cities': city,
               'tours': tours,
               'events': events
               }
    return render(request, "index/index.html", context)



