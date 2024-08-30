from django.shortcuts import render, redirect, get_object_or_404

from libros.api_method import create_libro, update_libro, delete_libro
from libros.forms import FormularioAutor, FormularioLibroModel, LibroForm
from libros.models import Libro, Autor


# __________________________________________________________________________________#
# Marcela CRUD
# __________________________________________________________________________________#
def home(request):
    form_creacion = LibroForm(prefix="create")
    form_actualizacion = LibroForm(prefix="update")

    return render(request, 'libros/home.html',{
        'create_form': form_creacion,
        'update_form': form_actualizacion
    })


# __________________________________________________________________________________#
# Kendrick CRUD
# __________________________________________________________________________________#
def inicio(request):
    # form = FormularioLibros()
    form = FormularioLibroModel()
    libros = Libro.objects.all()

    if create_libro(request):
        return redirect('libro')

    return render(request, 'libros/libro.html', {"libros": libros, "form": form})


def editar_libro(request, pk):
    libro = get_object_or_404(Libro.objects.all(), pk=pk)

    if update_libro(request, libro):
        return redirect('libro')

    return render(request, 'libros/editar_libro.html', {"form": FormularioLibroModel(instance=libro)})


def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro.objects.all(), pk=pk)

    delete_libro(request, libro)

    return redirect('libro')


def autor(request):
    form = FormularioAutor()
    autores = Autor.objects.all()

    if request.method == 'POST':
        form_request = FormularioAutor(request.POST)
        if form_request.is_valid():
            Autor.objects.create(
                nombre=form_request.cleaned_data['nombre'],
                apellidos=form_request.cleaned_data['apellidos'],
            )
            return redirect('autor')

    return render(request, 'libros/autor.html', {"form": form, "autores": autores})
