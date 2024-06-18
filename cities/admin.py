from django.contrib import admin
from . models import City, Excursions
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.safestring import mark_safe


class CityAdminForm(forms.ModelForm):
    info = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = City
        fields = '__all__'


class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm
    fields = ('title', 'preview', 'info', 'city_image', 'get_img_1', 'link_site_city')
    list_display = ('title', 'preview', 'get_img', 'link_site_city')
    list_filter = ('title',)
    search_fields = ('title', )
    readonly_fields = ('get_img_1',)
    list_per_page = 10

    def get_img(self, objects):
        if objects.city_image:
            return mark_safe(f"<img src='{objects.city_image.url}' width='100'>")
        else:
            return "not image"

    def get_img_1(self, objects):
        if objects.city_image:
            return mark_safe(f"<img src='{objects.city_image.url}' width='150'>")
        else:
            return "not image"

    get_img.short_description = 'Изображение'


class ExcursionsAdmin(admin.ModelAdmin):
    fields = ('owner', 'title', 'excursions_image', 'get_img_1', 'link', 'description', 'price', 'duration')
    list_display = ('owner', 'title', 'price', 'duration', 'get_img')
    list_display_links = ('title', 'owner')
    search_fields = ('title', 'price', 'duration')
    list_editable = ('price', 'duration')
    readonly_fields = ('get_img_1',)
    list_per_page = 10

    def get_img(self, objects):
        if objects.excursions_image:
            return mark_safe(f"<img src='{objects.excursions_image.url}' width='100'>")
        else:
            return "not image"

    def get_img_1(self, objects):
        if objects.excursions_image:
            return mark_safe(f"<img src='{objects.excursions_image.url}' width='150'>")
        else:
            return "not image"

    get_img.short_description = 'Изображение'


admin.site.register(City, CityAdmin)
admin.site.register(Excursions, ExcursionsAdmin)
