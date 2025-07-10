# Importa el formulario de creación de usuarios incorporado en Django.
from django.contrib.auth.forms import UserCreationForm


# Importa el modelo de usuario de Django.
from django.contrib.auth.models import User


# Importa el módulo de formularios para crear formularios personalizados.
from django import forms


# Importa el modelo personalizado Record.
from .models import Record


# Formulario de registro personalizado basado en UserCreationForm.
class SignUpForm(UserCreationForm):
    # Campo de correo electrónico.
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'})
    )


    # Campo de primer nombre.
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
    )


    # Campo de apellido.
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'})
    )


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)


        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = (
            '<span class="form-text text-muted"><small>'
            'Requerido. 150 caracteres o menos. Solo letras, números y @/./+/-/_.'
            '</small></span>'
        )


        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = (
            '<ul class="form-text text-muted small">'
            '<li>La contraseña no debe parecerse a tu información personal.</li>'
            '<li>Debe contener al menos 8 caracteres.</li>'
            '<li>No debe ser una contraseña comúnmente usada.</li>'
            '<li>No debe ser totalmente numérica.</li>'
            '</ul>'
        )


        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = (
            '<span class="form-text text-muted"><small>'
            'Introduce la misma contraseña que antes, para verificación.'
            '</small></span>'
        )


# Formulario para agregar registros del modelo Record.
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Nombre", "class": "form-control"}),
        label=""
    )


    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Apellido", "class": "form-control"}),
        label=""
    )


    email = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Correo electrónico", "class": "form-control"}),
        label=""
    )


    phone = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Teléfono", "class": "form-control"}),
        label=""
    )


    address = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Dirección", "class": "form-control"}),
        label=""
    )


    city = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Ciudad", "class": "form-control"}),
        label=""
    )


    state = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Departamento/Estado", "class": "form-control"}),
        label=""
    )


    zipcode = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Código postal", "class": "form-control"}),
        label=""
    )


    class Meta:
        model = Record
        exclude = ("user",)  # Este campo se puede asignar automáticamente en la vista.
