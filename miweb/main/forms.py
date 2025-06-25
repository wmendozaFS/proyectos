from django import forms
from .models import Proyecto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre','usuarios', 'descripcion']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not re.match(r'^[A-Z][a-zA-Z\s]{2,}$', nombre):
            raise forms.ValidationError("El nombre debe comenzar en mayúscula y tener al menos 3 letras.")
        return nombre
    
class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match(r'^[a-zA-Z0-9]{4,20}$', username):
            raise forms.ValidationError("El nombre de usuario debe tener entre 4 y 20 caracteres alfanuméricos.")
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not re.match(r'^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]{1,30}$', first_name):
            raise forms.ValidationError("El nombre debe comenzar en mayúscula y no contener símbolos.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not re.match(r'^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]{1,30}$', last_name):
            raise forms.ValidationError("El apellido debe comenzar en mayúscula y no contener símbolos.")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[\\w\\.]+@[\\w\\.-]+\\.\\w{2,4}$', email):
            raise forms.ValidationError("Introduce un correo electrónico válido.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return email
