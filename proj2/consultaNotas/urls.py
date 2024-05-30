from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_nota, name='agregar_nota'),
    path('', views.lista_notas, name='lista_notas')
]