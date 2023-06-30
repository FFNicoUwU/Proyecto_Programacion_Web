from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.register, name='registro'),
    path('productos/', views.productos, name= 'productos')
]