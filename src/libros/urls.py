from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('', views.inicio, name='index'),
    #path('<int:libro_id>', views.detalle_libro, name='libros_detalle'),
    #path('editar/<int:libro_id>', views.editar_libro, name='libros_editar'),
    #path('nuevo/', views.nuevo_libro, name='libros_nuevo'),
    #path('eliminar/<int:libro_id>', views.eliminar_libro, name='libros_eliminar'),
]