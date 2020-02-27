from django.urls import path

from . import views

app_name = 'calcGET'
urlpatterns = [
    path('', views.main, name='main'),
]
