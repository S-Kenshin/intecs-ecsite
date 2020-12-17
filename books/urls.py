from django.urls import path
from .views import Index

urlpatterns = [
    path('top/', Index.as_view(), name='index'),
]