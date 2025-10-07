from django.urls import path
from ProyectWebAPP import views 

urlpatterns = [
    path('', views.Home, name="Home"),
    path('Precios/', views.Precios, name="Precios"),
    path('Contacto/', views.Contacto, name="Contacto"),
    path('Servicios/', views.Servicios, name="Servicios"),
    path('Tienda/', views.Tienda, name="Tienda"),
    
]