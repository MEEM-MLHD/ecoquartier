from django.shortcuts import render
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Sum

from .models import Project
from .filters import ProjectFilter
from .forms import ProjectForm, ProjectEditorForm


def home(request):
    f = ProjectFilter(request.GET, queryset=Project.objects.all())
    label_ecoquartier = Project.objects.filter(label_ecoquartier__id=3).count()
    engaged_ecoquartier = Project.objects.filter(label_ecoquartier__id=2).count()
    logements = Project.objects.aggregate(Sum('logements'))
    renouvellement_urbain = Project.objects.filter(type_operation__id=2).count()
    total = Project.objects.all().count()
    percent_renouvellement_urbain = int(renouvellement_urbain/float(total)*100)
    geojson = GeoJSONSerializer().serialize(f.qs,
          geometry_field='coordonnees_geographiques',
          properties=('nom', 'commune', 'description', 'commune_label', 'short_description', 'feature', 'url'))
    return render(request, 'home.html', {
        'filter': f, 'geojson': geojson,
        'label_ecoquartier':label_ecoquartier,
        'engaged_ecoquartier':engaged_ecoquartier,
        'logements': logements,
        'percent_renouvellement_urbain': percent_renouvellement_urbain
    })


def profile(request):
    user = request.user
    projects_owner = Project.objects.filter(owner=request.user)
    projects_editor = Project.objects.filter(editors=request.user)
    return render(request, 'profile.html', {
        'user': user,
        'projects_owner': projects_owner,
        'projects_editor': projects_editor
    })


def engagement(request, pk, id):
    project = Project.objects.get(id=pk)
    return render(request, 'projects/project_engagement_detail.html', {
        'project': project,
        'engagement_id': id
    })


class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ProjectCreateView, self).form_valid(form)


class ProjectEditorUpdateView(UpdateView):
    model = Project
    form_class = ProjectEditorForm
    template_name = 'projects/project_editors_form.html'

