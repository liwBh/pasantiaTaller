from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('', views.inicio, name='index'),
    path('autor', views.autor, name='autor'),
    path('editar/<int:pk>', views.editar_libro, name='editar_libro'),
    path('eliminar/<int:pk>', views.eliminar_libro, name='eliminar_libro'),
]