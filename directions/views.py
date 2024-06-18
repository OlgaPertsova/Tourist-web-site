from django.contrib import messages
from django.db.models import Avg
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator
from telegram.sendmessage import send_tg
from django.contrib.auth.models import User


def directions(request, type_id=None):
    types = TypesRecreation.objects.all()
    context = {
        'types': types,
    }
    if type_id:
        tours = Tours.objects.filter(owner_id=type_id)
    else:
        tours = Tours.objects.all()

    paginator = Paginator(tours, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({'tours': page_obj})
    return render(request, 'directions/list_of_tours.html', context)


def direction(request, pk):
    spec_tour = Tours.objects.get(id=pk)
    rev_count = spec_tour.review_set.all().count()
    form_rev = ReviewForm()
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            tel = request.POST.get('tel')
            nik_tg = request.POST.get('nik_tg')
            people = request.POST.get('people')
            date_pr = request.POST.get('date_pr')
            element = Order(order_name=name,
                            order_email=email,
                            order_tel=tel,
                            order_nik_tg=nik_tg,
                            order_people=people,
                            order_date=date_pr,
                            )
            element.save()
            send_tg(tg_name=name, tg_email=email, tg_tel=tel,
                    tg_nik=nik_tg, tg_people=people, tg_date=date_pr)
            messages.success(request, "Ваша заявка принята! В течение суток с Вами свяжется администратор!")
            return redirect('directions')

    if request.method == "POST":
        form_rev = ReviewForm(request.POST)
        if form_rev.is_valid():
            body = form_rev.clean_text(request)
            if not body:
                review = form_rev.save(commit=False)
                review.tour = spec_tour
                review.owner = request.user.profile
                review.save()
                spec_tour.get_stars_count()
                messages.success(request, "Спасибо за отзыв!")

            return redirect('direction', pk=spec_tour.id)

    context = {
        'tour': spec_tour,
        'types': TypesRecreation.objects.all(),
        'form': form_rev,
        'form_book': form,
        'rev_count': rev_count
    }
    return render(request, 'directions/specific_tour.html', context)


def book_tour(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            tel = request.POST.get('tel')
            nik_tg = request.POST.get('nik_tg')
            people = request.POST.get('people')
            date_pr = request.POST.get('date_pr')
            element = Order(order_name=name,
                            order_email=email,
                            order_tel=tel,
                            order_nik_tg=nik_tg,
                            order_people=people,
                            order_date=date_pr,
                            )
            element.save()
            send_tg(tg_name=name, tg_email=email, tg_tel=tel,
                    tg_nik=nik_tg, tg_people=people, tg_date=date_pr)
            messages.success(request, "Ваша заявка принята! В течение суток с Вами свяжется администратор!")
            return redirect('directions')

    context = {
        'types': TypesRecreation.objects.all(),
        'form_book': form,
    }

    return render(request, 'directions/book_tour.html', context)


