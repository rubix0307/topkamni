from django.urls import path, include
from .views import *
urlpatterns = [

    path('', index, name='home'),
    path('category/<str:slug>', NewsFromCategory.as_view(), name='category-detail'),

]