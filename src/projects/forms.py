# -*- coding: utf-8 -*-
from dal import autocomplete
from django.contrib.gis import forms
from leaflet.forms.fields import GeometryCollectionField

from .models import Project, Commune


class ProjectForm(forms.ModelForm):
    european_network = forms.BooleanField(
        label=u"Etre visible sur le réseau européen des villes et territoires durables (<a target='_blank' href='http://rfsc.eu/'>RFSC</a>)",
        required=False
    )
    commune = forms.ModelChoiceField(
        label="Commune principale",
        help_text=u"Sur quelle commune est situé l'ÉcoQuartier",
        queryset=Commune.objects.all(),
        widget=autocomplete.ModelSelect2(url='commune-autocomplete')
    )
    communes = forms.ModelMultipleChoiceField(
        label="Autres communes",
        help_text="Si le projet est sur plusieurs communes",
        queryset=Commune.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='commune-autocomplete'),
        required=False
    )
    coordonnees_geographiques = GeometryCollectionField(
        label="Localisation du projet",
        help_text=u"Dessiner sur la carte la zone où se trouve votre projet",
    )

    class Meta:
        model = Project
        fields = ['nom', 'commune', 'communes', 'project_manager_lastname', 'project_manager_firstname', 'project_manager_mail', 'project_manager_structure', 'coordonnees_geographiques', 'type_operations', 'vocations', 'description', 'demarches', 'tags', 'charte']


class ProjectEditorForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['editors', ]
        widgets = {
            'editors': autocomplete.ModelSelect2Multiple(url='editor-autocomplete')
        }