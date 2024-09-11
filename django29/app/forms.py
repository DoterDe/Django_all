from .models import Author
from django.contrib.auth.forms import UserCreationForm
from django import forms
class SignUpForm(UserCreationForm):
    class Meta:
        model = Author
        fields = ('username', 'first_name', 'last_name', 'email','password1', 'password2','avatar','id_photo_front','id_photo_back','birthdate','profession','portfolio')
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
        }