from django.urls import path
from . import views as list_views

urlpatterns = [
    path('home/', list_views.home, name='list-home')
]