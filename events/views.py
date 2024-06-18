from django.shortcuts import render
from .models import *


def events(request):
    new = News.objects.all().order_by('-id')[:2]
    lifehacks = LifeHacks.objects.all()
    festivals = Festival.objects.all()
    months = Months.objects.all().order_by('id')

    context = {
        'news': new,
        'lifehacks': lifehacks,
        'festivals': festivals,
        'months': months
    }

    return render(request, "events/events.html", context)

