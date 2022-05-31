from django.urls import path
from familia import views

#Se crea las rutas
urlpatterns = [
    path('', views.index, name="index"),
    path('agregar/', views.agregar, name="agregar"),
    path('borrar/<identificador>', views.borrar, name="borrar"),
    path('buscar/', views.buscar, name="buscar"),
]