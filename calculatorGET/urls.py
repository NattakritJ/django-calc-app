from django.urls import path

from . import views

app_name = 'tinder'
urlpatterns = [
    path('', views.main, name='main'),
]
