from django.urls import path
from .views import post_list

urlpatterns = [
    path('top', post_list, name='index'),
]
