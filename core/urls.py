# urls for main_site/core
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]