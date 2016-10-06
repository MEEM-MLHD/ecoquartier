#from django.forms import ModelForm
from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    charte = forms.FileField(required=False)
    european_network = forms.BooleanField(required=False)

    class Meta:
        model = Project
        fields = ['nom', 'commune', 'contact', 'adresse', 'contexte_commune', 'contexte_site', 'type_operation', 'vocation', 'zonage_insee', 'procedure', 'description']