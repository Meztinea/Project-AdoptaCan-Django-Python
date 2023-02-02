from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mascota/<int:id>',views.get_mascota, name='mascota')
]

