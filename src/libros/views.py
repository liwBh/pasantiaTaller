
from django.shortcuts import render, redirect, get_object_or_404
from libros.models import Libro, Autor
from libros.forms import FormularioAutor, FormularioLibros, FormularioLibroModel
from libros.api import create_libro, update_libro, delete_libro

def inicio(request):
    #form = FormularioLibros()
    form = FormularioLibroModel()
    libros = Libro.objects.all()

    if create_libro(request):
        return redirect('libros:index')


    return render(request, 'libros/index.html', {"libros": libros, "form": form})

def editar_libro(request, pk):
    libro = get_object_or_404(Libro.objects.all(), pk=pk)

    if update_libro(request, libro):
        return redirect('libros:index')

    return render(request, 'libros/editar_libro.html', {"form": FormularioLibroModel(instance=libro)})

def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro.objects.all(), pk=pk)

    delete_libro(request, libro)

    return redirect('libros:index')


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
            return redirect('libros:autor')

    return render(request, 'libros/autor.html', {"form": form, "autores": autores})
