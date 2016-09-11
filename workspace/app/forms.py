from django.contrib.auth.models import User
from django import forms
from models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'is_staff']
        
class MascotaForm (forms.ModelForm):
    
    class Meta:
        model = Mascota
        fields = ['nombre_de_mascota', 'peso' , 'edad' , 'tipo_sangre' , 'nombre_contacto', 'numero_contacto' , 'nombre_veterinario']