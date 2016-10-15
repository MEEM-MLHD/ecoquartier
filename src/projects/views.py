from django.shortcuts import render
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Count, Sum

from .models import Project
from .filters import ProjectFilter
from .forms import ProjectForm, ProjectEditorForm


def home(request):
    f = ProjectFilter(request.GET, queryset=Project.objects.all().order_by('-mise_a_jour'))
    label_ecoquartier = Project.objects.filter(label_ecoquartier__id=3).count()
    label_ecoquartier_engage = Project.objects.filter(label_ecoquartier__id=2).count()
    engaged_ecoquartier = Project.objects.filter(label_ecoquartier__id=2).count()
    logements = Project.objects.filter(label_ecoquartier__id=3).aggregate(Sum('logements'))
    renouvellement_urbain = Project.objects.filter(type_operation__id=2).filter(label_ecoquartier__id__in=[3, 2]).count()
    anru = Project.objects.filter(type_operation__id=1).filter(label_ecoquartier__id__in=[3, 2]).count()
    total = Project.objects.all().count()
    print '>>>>', renouvellement_urbain+anru
    print '>>>>', label_ecoquartier
    percent_renouvellement_urbain = int((renouvellement_urbain+anru)/float(label_ecoquartier+label_ecoquartier_engage)*100)
    annee_label = Project.objects.exclude(annee_label__isnull=True).order_by('annee_label').values('annee_label').annotate(Count('annee_label'))
    geojson = GeoJSONSerializer().serialize(f.qs,
          geometry_field='coordonnees_geographiques',
          properties=('nom', 'commune', 'description', 'commune_label', 'short_description', 'feature', 'url', 'state'))
    return render(request, 'home.html', {
        'filter': f, 'geojson': geojson,
        'label_ecoquartier':label_ecoquartier,
        'engaged_ecoquartier':engaged_ecoquartier,
        'logements': logements,
        'percent_renouvellement_urbain': percent_renouvellement_urbain,
        'annee_label': annee_label
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

    def get_context_data(self, **kwargs):
        current_object = self.get_object()
        geojson = GeoJSONSerializer().serialize([current_object, ],
          geometry_field='coordonnees_geographiques',
          properties=('nom', 'description', 'commune_label', 'short_description', 'feature', 'url', 'state'))
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['geojson'] = geojson
        return context

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

