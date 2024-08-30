from django_filters import DateFromToRangeFilter, ChoiceFilter
from django_filters.rest_framework import FilterSet
from djgentelella.fields.drfdatetime import DateRangeTextWidget
from libros.models import Libro

class LibroFilter(FilterSet):
    fecha_publicacion = DateFromToRangeFilter(
        widget=DateRangeTextWidget(attrs={'placeholder': 'YYYY/MM/DD'}))
    categoria = ChoiceFilter(choices=Libro.CATEGORIAS)

    class Meta:
        model = Libro
        fields = {
            "id": ["exact"],
            'nombre': ['icontains'],
            'categoria': ['icontains'],
            'autor__nombre': ['icontains'],
            'autor__apellidos': ['icontains'],
            'fecha_publicacion': ['gte', 'lte'],
        }