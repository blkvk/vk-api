from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analize/', views.analize, name='analize')
]
