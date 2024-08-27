from django.shortcuts import render
from libros.models import Libro
def inicio(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {"libros": libros})
