from django.urls import path
from Linear import views

urlpatterns = [
    path(route='',view=views.Home,name='Home'),
]
