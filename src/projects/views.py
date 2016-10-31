# -*- coding: utf-8 -*-
import collections

from django.shortcuts import render
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Count, Sum

from .models import Project
from .filters import ProjectFilter
from .forms import ProjectForm, ProjectEditorForm, ProjectEngagement1Form, ProjectEngagement2Form, ProjectEngagement3Form, ProjectEngagement4Form, ProjectEngagement5Form, ProjectEngagement6Form, ProjectEngagement7Form, ProjectEngagement8Form, ProjectEngagement9Form, ProjectEngagement10Form, ProjectEngagement11Form, ProjectEngagement12Form, ProjectEngagement13Form, ProjectEngagement14Form, ProjectEngagement15Form, ProjectEngagement16Form, ProjectEngagement17Form, ProjectEngagement18Form, ProjectEngagement19Form, ProjectEngagement20Form


def home(request):
    f = ProjectFilter(request.GET, queryset=Project.objects.all().order_by('-mise_a_jour'))
    label_ecoquartier = Project.objects.filter(label_ecoquartier__id=3).count()
    label_ecoquartier_engage = Project.objects.filter(label_ecoquartier__id=2).count()
    engaged_ecoquartier = Project.objects.filter(label_ecoquartier__id=2).count()
    logements = Project.objects.filter(label_ecoquartier__id=3).aggregate(Sum('logements'))
    renouvellement_urbain = Project.objects.filter(type_operations__id=2).filter(label_ecoquartier__id__in=[3,]).count()
    anru = Project.objects.filter(type_operations__id=1).filter(label_ecoquartier__id__in=[3,]).count()
    total = Project.objects.all().count()
    percent_renouvellement_urbain = int((renouvellement_urbain+anru)/float(label_ecoquartier)*100)

    annee_label = Project.objects.exclude(annee_label__isnull=True).order_by('annee_label').values('annee_label').annotate(Count('annee_label'))
    annee_candidature = Project.objects.exclude(annee_candidature__isnull=True).order_by('annee_candidature').values('annee_candidature').annotate(Count('annee_candidature'))
    annee_charte = Project.objects.exclude(charte_date__isnull=True).extra(select={'year':"CAST(EXTRACT(YEAR FROM charte_date) AS INTEGER)"}).values('year').annotate(Count('id'))

    chart_data = {}
    labels = [annee['annee_candidature'] for annee in annee_candidature]
    dataset_anne_candidature = [annee['annee_candidature__count'] for annee in annee_candidature]
    chart_data["labels"] = labels

    search = False
    if len(request.GET) > 0:
        search = True

    annee_label2 = {item['annee_label']: item['annee_label__count'] for item in annee_label}
    annee_charte2 = {item['year']: item['id__count'] for item in annee_charte}
    for year in labels:
        if year not in annee_label2.keys():
            annee_label2[year] = 0
        if year not in annee_charte2.keys():
            annee_charte2[year] = 0

    annee_label_data = collections.OrderedDict(sorted(annee_label2.items()))
    annee_charte_data = collections.OrderedDict(sorted(annee_charte2.items()))

    chart_data["datasets"] = [
        {"label": u"Charte signée", "data":annee_charte_data.values()},
        {"label": u"Engagé", "data":dataset_anne_candidature},
        {"label": u"Labellisé", "data":annee_label_data.values()},
        ]

    geojson = GeoJSONSerializer().serialize(f.qs,
          geometry_field='coordonnees_geographiques',
          properties=('nom', 'commune', 'description', 'commune_label', 'short_description', 'feature', 'url', 'state'))
    return render(request, 'home.html', {
        'filter': f, 'geojson': geojson,
        'label_ecoquartier':label_ecoquartier,
        'engaged_ecoquartier':engaged_ecoquartier,
        'logements': logements,
        'percent_renouvellement_urbain': percent_renouvellement_urbain,
        'chart_data': chart_data,
        'search': search
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
    if request.method == 'POST':
        form = eval('ProjectEngagement'+str(id)+'Form')(request.POST, instance=project)
        if form.is_valid():
            form.save()
    else:
        form = eval('ProjectEngagement'+str(id)+'Form')(instance=project)
    return render(request, 'projects/project_engagement_detail.html', {
        'project': project,
        'engagement_id': int(id),
        'form': form
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

