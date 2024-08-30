
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView
from djgentelella.urls import urlpatterns as djgentelellaurls

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from libros.urls import urlpatterns as libros_urls

schema_view = get_schema_view(
   openapi.Info(
      title="Taller SOLVO",
      default_version='v1',
      description="Taller para pasantes 2024",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = djgentelellaurls + [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='redocs'),
    path('libros/', include((libros_urls, 'libros'), namespace="libros")),
    path('', RedirectView.as_view(url=reverse_lazy('libros:home')), name='home'),
]
