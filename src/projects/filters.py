import django_filters
from django import forms
from projects.models import Project, ZonageINSEE, LabelEcoQuartier, TypeOperation


class ProjectFilter(django_filters.FilterSet):
    zonage_insee = django_filters.filters.ModelMultipleChoiceFilter(queryset=ZonageINSEE.objects.all(), widget=forms.CheckboxSelectMultiple)
    type_operation = django_filters.filters.ModelMultipleChoiceFilter(queryset=TypeOperation.objects.all(), widget=forms.CheckboxSelectMultiple)
    label_ecoquartier = django_filters.filters.ModelMultipleChoiceFilter(queryset=LabelEcoQuartier.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Project
        fields = ['label_ecoquartier', 'type_operation', 'zonage_insee']