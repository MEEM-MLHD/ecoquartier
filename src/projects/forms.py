from dal import autocomplete
from django import forms

from .models import Project, Commune


class ProjectForm(forms.ModelForm):
    charte = forms.FileField(required=False)
    european_network = forms.BooleanField(required=False)
    commune = forms.ModelChoiceField(
        queryset=Commune.objects.all(),
        widget=autocomplete.ModelSelect2(url='commune-autocomplete')
    )


    class Meta:
        model = Project
        fields = ['nom', 'commune', 'contact', 'adresse', 'contexte_commune', 'contexte_site', 'type_operation', 'vocation', 'zonage_insee', 'procedure', 'description']
