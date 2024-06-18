from django.contrib import admin
from . models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class FestivalAdminForm(forms.ModelForm):
    info = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = City
        fields = '__all__'


class FestivalAdmin(admin.ModelAdmin):
    form = FestivalAdminForm
    fields = ('owner', 'title', 'link', 'date_of_the', 'info', 'css')
    list_display = ('owner', 'title', 'link', 'date_of_the', 'css')
    list_filter = ('title',)
    search_fields = ('title', )
    list_editable = ('title', 'link', 'date_of_the', 'css')


admin.site.register(Months)
admin.site.register(News)
admin.site.register(LifeHacks)
admin.site.register(Festival, FestivalAdmin)

