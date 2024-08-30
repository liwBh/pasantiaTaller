from django import forms
from djgentelella.forms.forms import GTForm
from djgentelella.widgets import core as GTWidget

from libros.models import Autor, Libro


#__________________________________________________________________________________#
# Marcela CRUD
#__________________________________________________________________________________#

class LibroForm(GTForm, forms.ModelForm):

    class Meta:
        model = Libro
        #fields = '__all__'
        exclude = ["fecha_actualizacion"]
        widgets = {
            "autor": GTWidget.Select(),
            "nombre": GTWidget.TextInput(),
            "categoria": GTWidget.Select(),
            "fecha_publicacion": GTWidget.DateInput(),
        }

#__________________________________________________________________________________#
# Kendrick CRUD
#__________________________________________________________________________________#
class FormularioAutor(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre",
                             widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    apellidos = forms.CharField(max_length=50, label="Apellidos",
                                widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)


class FormularioLibros(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control'}),
                             required=True)
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), label="Autor",
                                   widget=forms.Select(attrs={'class': 'form-select'}), required=True)
    categoria = forms.ChoiceField(choices=Libro.CATEGORIAS, initial=Libro.CATEGORIAS[0], label="Categoría",
                                  widget=forms.Select(attrs={'class': 'form-select'}), required=True)
    fecha_publicacion = forms.DateField(label="Fecha Publicación",
                                        widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)


class FormularioLibroModel(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['autor'].queryset = Autor.objects.all()
        self.fields['autor'].required = True

        self.fields['fecha_publicacion'].required = True

        self.fields['nombre'].label = "Nombre"
        self.fields['nombre'].required = True
        self.fields['nombre'].max_length = 50

        self.fields['categoria'].required = True
        self.fields['categoria'].initial = 0

    class Meta:
        model = Libro
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'fecha_publicacion': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': '2024-01-01', 'type': 'date'}),
        }
        #fields = '__all__'  # especifica los campos que quieres incluir explícitamente.
        exclude = ['fecha_actualizacion']  # especifica los campos que quieres excluir explícitamente.
