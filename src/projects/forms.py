from dal import autocomplete
from django.contrib.gis import forms
from leaflet.forms.fields import GeometryCollectionField

from .models import Project, Commune


class ProjectForm(forms.ModelForm):
    european_network = forms.BooleanField(required=False)
    commune = forms.ModelChoiceField(
        queryset=Commune.objects.all(),
        widget=autocomplete.ModelSelect2(url='commune-autocomplete')
    )
    communes = forms.ModelMultipleChoiceField(
        queryset=Commune.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='commune-autocomplete'),
        required=False
    )
    coordonnees_geographiques = GeometryCollectionField()

    class Meta:
        model = Project
        fields = ['nom', 'commune', 'communes', 'contact', 'adresse', 'coordonnees_geographiques', 'contexte_commune', 'contexte_site', 'type_operations', 'vocation', 'description', 'demarches', 'tags', 'charte']


class ProjectEditorForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['editors', ]
        widgets = {
            'editors': autocomplete.ModelSelect2Multiple(url='editor-autocomplete')
        }