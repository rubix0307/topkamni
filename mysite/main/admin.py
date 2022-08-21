from django.contrib import admin
from .models import Category
# Register your models here.

class Category_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_show_in_main_navigation', 'is_show_in_social_links')
    list_display_links = ('slug',)
    list_editable = ('is_show_in_main_navigation', 'is_show_in_social_links',)
    search_fields = ('title',)


admin.site.register(Category, Category_admin)