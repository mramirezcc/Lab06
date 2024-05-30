from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_venta, name="crear_venta"),
    path('lista/', views.lista_ventas, name='lista_ventas')
]