# -*- coding: utf-8 -*-
from dal import autocomplete
from django.contrib.gis import forms
from leaflet.forms.fields import GeometryCollectionField

from .models import Project, Commune, Demarche, TypeOperation, Vocation, Tag


class ProjectForm(forms.ModelForm):
    european_network = forms.BooleanField(
        label=u"Etre visible sur le réseau européen des villes et territoires durables (<a target='_blank' href='http://rfsc.eu/fr/'>RFSC</a>)",
        required=False,
        help_text=u"En cochant cette case, la fiche d'identité de votre projet sera visible sur le site du 'cadre de référence des villes et territoires durables', favorisant la mise en réseau des collectivités européennes ayant des expériences en matière d'aménagement durable."
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

    type_operations = forms.ModelMultipleChoiceField(label=u"Type d'opérations (plusieurs choix possibles)", queryset=TypeOperation.objects.all(), widget=forms.CheckboxSelectMultiple(),required=False)
    vocations = forms.ModelMultipleChoiceField(label=u"Vocations (plusieurs choix possibles)", queryset=Vocation.objects.all(), widget=forms.CheckboxSelectMultiple(),required=False)
    demarches = forms.ModelMultipleChoiceField(label=u"Engagement dans d'autres démarches de développement durable (plusieurs choix possibles)", queryset=Demarche.objects.all(), widget=forms.CheckboxSelectMultiple(),required=False)
    tags = forms.ModelMultipleChoiceField(label=u"Points forts du projet (plusieurs choix possibles dans la limite de 5)", queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple(),required=False)

    class Meta:
        model = Project
        fields = ['nom', 'commune', 'communes', 'project_manager_lastname', 'project_manager_firstname', 'project_manager_mail', 'project_manager_structure', 'project_developer_lastname', 'project_developer_firstname', 'project_developer_mail', 'project_developer_structure', 'plusieurs_tranches', 'coordonnees_geographiques', 'type_operations', 'vocations', 'procedure', 'description', 'demarches', 'demarches_autres', 'tags', 'charte']


class ProjectEditorForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['editors', ]
        widgets = {
            'editors': autocomplete.ModelSelect2Multiple(url='editor-autocomplete')
        }


class GlobalProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['plan_situation_1_5000', 'plan_masse_1_1000', 'plan_masse_1_500', 'plan_detaille', 'maitrise_ouvrage_structure', 'maitrise_ouvrage_nom',]


class ProjectEngagement1Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_1']


class ProjectEngagement2Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_2']


class ProjectEngagement3Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_3']


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
        fields = ['engagement_6']


class ProjectEngagement7Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_7']


class ProjectEngagement8Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_8']


class ProjectEngagement9Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_9']


class ProjectEngagement10Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_10']


class ProjectEngagement11Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_11']


class ProjectEngagement12Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['engagement_12']


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


class ProjectData1Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['site', 'contexte_site', 'superficieha', 'surface_nonbatie',  'engagement', 'creation', 'realisation', 'autorisation', 'permis', 'debut', 'livraison', 'achevement', 'etudes_prealables', 'opacrations_marquantes', 'habitants', 'logements', 'shon_logementsm', 'logements_sociau', 'logements_sociaux_detail', 'shon_equipementsm', 'equipements_publics', 'shon_commercesm', 'commerces_services', 'shon_bureauxm', 'bureaux_activites',]


class ProjectData2Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['procedure', 'procedure_detail', 'concertation', 'collectivite_ou_epci_porteur', 'maitrise_ouvrage', 'maitrise_oeuvre', 'partenariats', ]


class ProjectData3Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['coats', ]


class ProjectData4Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = []


class ProjectData5Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = []


class ProjectData6Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['aspects_fonciers', 'densite_brute', 'densite_brute_logements', 'densite_logements', 'surface_nonbatie', ]


class ProjectData7Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['habitants', 'logements', 'shon_logementsm', 'logements_sociau', ]


class ProjectData8Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['coats', ]


class ProjectData9Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['opacrations_marquantes', ]


class ProjectData10Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['contexte_site', ]


class ProjectData11Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['equipements_publics', 'shon_equipementsm', 'commerces_services', 'shon_commercesm', 'bureaux_activites', 'shon_bureauxm',]


class ProjectData12Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['equipements_publics', 'shon_equipementsm', 'commerces_services', 'shon_commercesm', 'bureaux_activites', 'shon_bureauxm',]


class ProjectData13Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = []


class ProjectData14Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = []


class ProjectData15Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = []


class ProjectData16Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = []


class ProjectData17Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = []


class ProjectData18Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = []


class ProjectData19Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = []


class ProjectData20Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = []
