from django.shortcuts import render
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Project
from .filters import ProjectFilter


def home(request):
    f = ProjectFilter(request.GET, queryset=Project.objects.all())
    geojson = GeoJSONSerializer().serialize(f.qs,
          geometry_field='coordonnees_geographiques',
          properties=('nom', 'commune', 'description', 'commune_label', 'short_description', 'feature', 'url'))
    return render(request, 'home.html', {
        'filter': f, 'geojson': geojson
    })


class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    fields = ['nom', 'departement', 'description']