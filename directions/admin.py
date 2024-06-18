from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class PhotoAdd(admin.StackedInline):
    model = Photo
    fields = ('tour', 'add_photo')
    extra = 0


class TourAdminForm(forms.ModelForm):
    program = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Tours
        fields = '__all__'


class TourAdmin(admin.ModelAdmin):
    form = TourAdminForm
    list_display = ('name', 'id', 'owner', 'price', 'rating')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'preview')
    list_editable = ('price', 'rating')
    inlines = [PhotoAdd]


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('tour', 'add_photo')


# class OrderAdmin(admin.ModelAdmin):
#     readonly_fields = ('order_name',)


admin.site.register(TypesRecreation)
admin.site.register(Tours, TourAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Order)
admin.site.register(Review)
