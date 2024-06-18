from django.contrib import admin
from .models import *


class MorePhotoAdd(admin.StackedInline):
    model = MorePhoto
    fields = ('place', 'owner', 'add_more_photo')
    extra = 0


class TravelDiaryAdmin(admin.ModelAdmin):
    fields = (('owner', 'place'), ('arrival_date', 'departure_date'),
              ('cafes', 'money_spend_on_eats'), ('housing', 'money_spend_on_housing'),
              ('entertainments', 'money_spend_on_entertainments'),
              'travel_image')
    inlines = [MorePhotoAdd]


admin.site.register(Profile)
admin.site.register(Places)
admin.site.register(TravelDiary, TravelDiaryAdmin)
admin.site.register(MorePhoto)
admin.site.register(Verification)
