from django.db import models
from django.db.models import CASCADE, SET_DEFAULT, SET_NULL

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellidos)
class Libro(models.Model):
    CATEGORIAS = (
        (0, "Sin definir"),
        (2, "Romance"),
        (3, "Acción"),
        (4, "Terror"),
        (4, "Comedia"),
    )
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    autor = models.ForeignKey(Autor, on_delete=CASCADE, verbose_name="Autor")
    fecha_publicacion = models.DateField(auto_now=True, verbose_name="Fecha Publicación")
    categoria = models.SmallIntegerField(choices=CATEGORIAS, default=0, verbose_name="Categoría")

    def __str__(self):
        return "%s - %s" % (self.nombre, self.autor.nombre)

#! Notas
'''
Cuando eliminamos un registro relacionado, podemos utilizar una de 
las siguientes opciones:

1. CASCADE:
   - Elimina todos los registros asociados al registro que se está eliminando.
   - Por ejemplo, si se elimina un autor, todos los libros asociados a ese 
     autor también se eliminan.

2. SET_DEFAULT:
   - Establece el valor de un campo relacionado al valor por defecto especificado 
     en ese campo.
   - Por ejemplo, si se elimina un autor y un libro tiene un campo que hace 
     referencia a ese autor, dicho campo se establecerá al valor por defecto 
     definido en el modelo, si es que tiene uno.

3. SET_NULL:
   - Establece el valor de un campo relacionado como `NULL` (nulo).
   - Por ejemplo, si se elimina un autor, el campo que referenciaba a ese 
     autor se establecerá en `NULL`, siempre y cuando el campo permita valores 
     nulos (`null=True` en la definición del campo).

'''