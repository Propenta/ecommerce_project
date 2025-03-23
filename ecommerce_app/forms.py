from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

class InscriptionForm(UserCreationForm):
    telephone = forms.CharField(max_length=15, required=False, help_text="Optionnel.")
    adresse = forms.CharField(max_length=255, required=False, help_text="Optionnel.")

    class Meta:
        model = Utilisateur
        fields = ('username', 'email', 'password1', 'password2', 'telephone', 'adresse')