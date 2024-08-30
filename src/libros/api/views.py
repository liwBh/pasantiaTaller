from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import authentication, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from rest_framework.permissions import BasePermission
from djgentelella.objectmanagement import AuthAllPermBaseObjectManagement
from rest_framework.views import APIView

from libros.api.serializers import LibroSerializer
from libros.models import Libro
from libros.api import serializers
from libros.api import filterset
class LibroManagentViewset(AuthAllPermBaseObjectManagement):
    serializer_class = {
        "list": serializers.LibroDataTableSerializer,
        "create": serializers.LibroValidateSerializer,
        "update": serializers.LibroValidateSerializer,
        "destroy": serializers.LibroSerializer,
    }

    perms = {
        "list": ["libros.view_libro"],
        "create": ["libros.add_libro"],
        "update": ["libros.change_libro"],
        "destroy": ["libros.delete_libro"],
    }

    permission_classes = (BasePermission,)

    queryset = Libro.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ["nombre", "autor__nombre", "autor__apellidos"]
    filterset_class = filterset.LibroFilter
    ordering_fields = ["nombre"]
    ordering = ("nombre",)

class ListBooks(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    serializer_class = LibroSerializer
    queryset = Libro.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = self.paginate_queryset(queryset)
        response = {'data': data}

        return Response(self.get_serializar(response).data)
