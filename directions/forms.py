from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib import messages


STOP_LIST = [
    'пиздец',
    'блять',
    'сука',
    'тварь',
    'охуеть',
    'дерьмо',
    'пидорас',
    'fuck',
]


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        choices = ((1, ''), (2, ''), (3, ''), (4, ''), (5, ''))
        widgets = {'body': forms.Textarea(attrs={'class': 'input', 'placeholder': 'Ваш отзыв...'}),
                   'value': forms.RadioSelect(attrs={'name': 'rate'}, choices=choices)
                   }

    def clean_text(self, request):
        text = self.cleaned_data["body"]
        for word in STOP_LIST:
            if word in text:
                messages.error(request, "Вы позволили себе немного лишнего! Одумайтесь и исправьте текст!")
                return text


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "input__group"}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "input__group"}))
    tel = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "input__group"}))
    nik_tg = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "input__group"}))
    people = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "input__group"}))
    date_pr = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={"class": "input__group", "type": "date"}))
