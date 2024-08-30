from django.utils import formats
from djgentelella.serializers import GTDateField
from djgentelella.serializers.selects import GTS2SerializerBase
from rest_framework import serializers

from libros.models import Libro, Autor


class LibroSerializer(serializers.ModelSerializer):
    autor__nombre = serializers.SerializerMethodField()
    autor__apellidos = serializers.SerializerMethodField()
    fecha_publicacion = GTDateField()
    categoria_display = serializers.SerializerMethodField()
    actions = serializers.SerializerMethodField()
    autor = GTS2SerializerBase()
    categoria = serializers.SerializerMethodField()

    def get_categoria(self, obj):
        return {
            "id": obj.categoria, "text": self.get_categoria_display(obj),
            "disabled": False, "selected": True
        }

    def get_autor__nombre(self, obj):
        return obj.autor.nombre

    def get_autor__apellidos(self, obj):
        return obj.autor.apellidos

    def get_categoria_display(self, obj):
        return obj.get_categoria_display()

    def get_actions(self, obj):
        return {
            "create": True,
            "update": True,
            "destroy": True,
            "detail": True,
        }

    class Meta:
        model = Libro
        fields = ["id", "nombre", "categoria", "categoria_display", "autor", "autor__nombre", "autor__apellidos",
                  "fecha_publicacion", "actions"]


class LibroDataTableSerializer(serializers.Serializer):
    data = serializers.ListField(child=LibroSerializer(), required=True)
    draw = serializers.IntegerField(required=True)
    recordsFiltered = serializers.IntegerField(required=True)
    recordsTotal = serializers.IntegerField(required=True)


class LibroValidateSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(max_length=50)
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    categoria = serializers.IntegerField(default=0, min_value=0)
    #fecha_publicacion = serializers.DateField()
    fecha_publicacion = serializers.DateField(
        input_formats=[formats.get_format('DATE_INPUT_FORMATS')[0]],
        format=formats.get_format('DATE_INPUT_FORMATS')[0])

    def validate(self, data):
        data = super().validate(data)
        nombre = data['nombre']

        if not (isinstance(nombre, str) and len(nombre) >= 3):
            raise serializers.ValidationError({"nombre": "El nombre debe contener mas de 3 caracteres"})

        return data

    class Meta:
        model = Libro
        exclude = ["fecha_actualizacion"]
