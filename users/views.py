from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from django.views.generic.base import TemplateView


def login_user(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request,"Пользователь с таким именем не найден!")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            messages.error(request,"Допущена ошибка при вводе имени или пароля!")
            return redirect("index")

    return render(request, "events/base.html")


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "Аккаунт успешно создан! "
                                      "Заполните полностью свой профиль - нажав на фото!")
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Допущена ошибка при регистрации!")
            return redirect("index")

    form = RegisterUserForm
    context = {'form': form}
    return render(request, "users/register.html", context)


def logout_user(request):
    logout(request)
    messages.info(request, "Вы вышли из своего аккаунта!")
    return redirect('index')


@login_required(login_url='index')
def profile(request):
    prof = request.user.profile
    place = prof.traveldiary_set.all()
    form = ProfileForm(instance=prof)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=prof)
        if form.is_valid():
            form.save()

            return redirect('profile')
    context = {
        "profile": prof,
        "places": place,
        'form': form,
    }

    return render(request, "users/profile.html", context)


def profile_form(request):
    prof = request.user.profile
    form = ProfileForm(instance=prof)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=prof)
        if form.is_valid():
            form.save()
            messages.error(request, "Перейдите на свою почту, чтобы пройти верификацию! Сообщение может быть в спаме!")
            return redirect('profile')

    context = {'form': form}
    return render(request, "users/profile_form.html", context)


class VerificationView(TemplateView):
    template_name = 'users/verification.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Путешествия по России - Подтверждение почты"
        return context

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = Profile.objects.get(email=kwargs['email'])
        verifications = Verification.objects.filter(user=user, code=code)
        if verifications.exists() and not verifications.first().is_expired():
            user.verify = True
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return redirect('index')


def create_place(request):
    prof = request.user.profile
    form_place = TravelDiaryForm()

    if request.method == "POST":
        form_place = TravelDiaryForm(request.POST, request.FILES)
        if form_place.is_valid():
            place = form_place.save(commit=False)
            place.owner = prof
            place.save()
            return redirect('travel_diary')

    context = {'form_place': form_place}
    return render(request, 'users/create_place.html', context)


def travel_diary(request):
    prof = request.user.profile
    place = prof.traveldiary_set.all()
    form_place = TravelDiaryForm()

    if request.method == "POST":
        form_place = TravelDiaryForm(request.POST, request.FILES)
        if form_place.is_valid():
            place = form_place.save(commit=False)
            place.owner = prof
            place.save()
            return redirect('travel_diary')

    context = {
        "profile": prof,
        "places": place,
        'form_place': form_place
    }

    return render(request, 'users/travel_diary.html', context)


def place(request, pk):
    prof = request.user.profile
    place = TravelDiary.objects.get(id=pk)
    form_photo = AddMorePhotoForm()

    if request.method == 'POST':
        form_photo = AddMorePhotoForm(request.POST, request.FILES)
        if form_photo.is_valid():
            photo = form_photo.save(commit=False)
            photo.owner = prof
            photo.place = place
            photo.save()
        else:
            form_photo = AddMorePhotoForm()
    context = {
        'place': place,
        'form_photo': form_photo
    }

    return render(request, 'users/specific_place.html', context)

