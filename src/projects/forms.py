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


class ProjectEngagement1Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['site', 'contexte_site', 'superficieha', 'surface_nonbatie',  'engagement', 'creation', 'realisation', 'autorisation', 'permis', 'debut', 'livraison', 'achevement', 'complementaire', 'programme_detail', 'etudes_prealables', 'opacrations_marquantes', 'habitants', 'logements', 'shon_logementsm', 'logements_sociau', 'equipements_publics', 'shon_equipementsm', 'commerces_services', 'shon_commercesm', 'bureaux_activites', 'shon_bureauxm', 'engagement_1', ]


class ProjectEngagement2Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['procedure', 'procedure_detail', 'concertation', 'collectivite_ou_epci_porteur', 'maitrise_ouvrage', 'maitrise_oeuvre', 'partenariats', 'engagement_2']


class ProjectEngagement3Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['coats', 'engagement_3']


class ProjectEngagement4Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_4']


class ProjectEngagement5Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_5']


class ProjectEngagement6Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['aspects_fonciers', 'densite_brute', 'densite_brute_logements', 'densite_logements', 'surface_nonbatie', 'engagement_6']


class ProjectEngagement7Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['habitants', 'logements', 'shon_logementsm', 'logements_sociau', 'engagement_7']


class ProjectEngagement8Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['coats', 'engagement_8']


class ProjectEngagement9Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['opacrations_marquantes', 'engagement_9']


class ProjectEngagement10Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['contexte_site', 'engagement_10']


class ProjectEngagement11Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['equipements_publics', 'shon_equipementsm', 'commerces_services', 'shon_commercesm', 'bureaux_activites', 'shon_bureauxm', 'engagement_11']


class ProjectEngagement12Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['equipements_publics', 'shon_equipementsm', 'commerces_services', 'shon_commercesm', 'bureaux_activites', 'shon_bureauxm', 'engagement_12']


class ProjectEngagement13Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_13']


class ProjectEngagement14Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_14']


class ProjectEngagement15Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_15']


class ProjectEngagement16Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_16']


class ProjectEngagement17Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_17']


class ProjectEngagement18Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_18']


class ProjectEngagement19Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_19']


class ProjectEngagement20Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_20']
