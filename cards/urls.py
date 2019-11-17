from django.urls import path

from . import views

urlpatterns = [
    path('<str:url_suffix>/', views.index, name='index'),
]