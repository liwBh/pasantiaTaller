from libros.forms import FormularioLibroModel
from libros.models import Libro
from django.contrib import messages


def get_errors(form):
    error_messages = []
    for field, errors in form.errors.items():
        field_label = form.fields[field].label
        for error in errors:
            error_messages.append(f"Error en {field_label}: {error}")

    # Combinar los mensajes de error en un solo string, separados por saltos de línea
    error_message = "\n".join(error_messages)

    return error_message


def create_libro(request):

    if request.method == 'POST':
        form = FormularioLibroModel(request.POST)

        if form.is_valid():
            messages.success(request, "Registro exitoso!")
            form.save()
            return True
        else:
            messages.error(request, get_errors(form))

    return False


def update_libro(request, libro):

    if request.method == 'POST':
        form = FormularioLibroModel(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.error(request, "Actualización exitosa!")
            return True
        else:
            messages.error(request, get_errors(form))

    return False


def delete_libro(request, libro):
    if libro:
        libro.delete()
        messages.success(request, "Registro eliminado!")
        return True
    else:
        messages.error(request, "No se pudo eliminar el registro!")

    return False