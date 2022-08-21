from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
from .models import Category, Post
# Register your models here.

# CKEditor
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_show_in_main_navigation', 'is_show_in_social_links')
    list_display_links = ('slug',)
    list_editable = ('is_show_in_main_navigation', 'is_show_in_social_links',)
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    save_as = True # save as new object
    save_on_top = True # button "save" on top
    # prepopulated_fields = {'slug': ('title',),}
    # нужные колонки
    list_display = ('id', 'title', 'photo','category', 'is_published','views', 'update_date', 'create_date')

    # ссылка на запись в админке
    list_display_links = ('id', 'title',)

    # поиск по
    search_fields = ('title',)

    # изменяемые поля прям с вписке всех записей
    list_editable = ('category', 'is_published','views')

    # фильтры в списке всех записей
    list_filter = ('category', 'is_published')
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)