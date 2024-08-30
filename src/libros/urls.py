from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from libros.api.views import LibroManagentViewset, ListBooks

objectrouter = DefaultRouter()
objectrouter.register('api_libro_list', LibroManagentViewset, basename="api-libro")

app_name = 'libros'

urlpatterns = [
    path('', views.home, name='home'),
    path('libro', views.inicio, name='libro'),
    path('autor', views.autor, name='autor'),
    path('editar/<int:pk>', views.editar_libro, name='editar_libro'),
    path('eliminar/<int:pk>', views.eliminar_libro, name='eliminar_libro'),
    path('api/', include(objectrouter.urls)),
    path('listado_libros_apiview', ListBooks.as_view(), name="apiview_books")
]