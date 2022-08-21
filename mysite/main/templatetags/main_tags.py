from django import template
from main.models import Category
from django.db.models import Count, F
from django.core.cache import cache
register = template.Library()





@register.inclusion_tag('main/nav.html')
def show_categories():
    
    main_navigation = Category.objects.filter(is_show_in_main_navigation=True)
    social_links = Category.objects.filter(is_show_in_social_links=True)

    context = {
        'main_navigation': main_navigation,
        'social_links': social_links,
    }

    return context