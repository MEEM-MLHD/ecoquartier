import django_filters

from projects.models import Project


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = ['statut', 'zonage_insee', 'departement', 'region', 'contexte_commune', 'type_operation', 'vocation', 'label_ecoquartier', 'procedure', ]