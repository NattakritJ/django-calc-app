from django.urls import path

from . import views

app_name = 'calcPOST'
urlpatterns = [
    path('', views.main, name='main'),
    path('aboutme/', views.aboutme, name='aboutme'),
]
