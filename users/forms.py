from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
from django import forms
import uuid
from datetime import timedelta
from django.utils.timezone import now


class TravelDiaryForm(ModelForm):
    class Meta:
        model = TravelDiary
        fields = '__all__'
        exclude = ['owner', ]
        widgets = {'arrival_date': forms.DateInput(format='%Y-%m-%d', attrs={"class": "input__group", "type": "date"}),
                   'departure_date': forms.DateInput(format='%Y-%m-%d', attrs={"class": "input__group", "type": "date"})
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "input__group"})


class AddMorePhotoForm(ModelForm):
    class Meta:
        model = MorePhoto
        fields = ['add_more_photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control mb-3"})


class PlaceForm(ModelForm):
    class Meta:
        model = Places
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "input__group"})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'bio', 'my_city',
                  'profile_image']

    def save(self, commit=True):
        user = super().save(commit=True)
        expiration = now() + timedelta(hours=24)
        record = Verification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})
