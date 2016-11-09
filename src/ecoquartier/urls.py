# -*- coding: utf-8 -*-
"""ecoquartier URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from djgeojson.views import GeoJSONLayerView

from projects import views
from projects.models import Project
from projects.autocompletes import CommuneAutocomplete, EditorAutocomplete


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^detail/(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='detail'),
    url(r'^interlocuteurs/(?P<code_insee>\w+)$', views.interlocuteurs, name='interlocuteurs'),
    url(r'^detail/(?P<pk>\d+)/engagement/(?P<id>\d+)', views.engagement, name='engagement'),
    url(r'^create/$', login_required(views.ProjectCreateView.as_view()), name='create'),
    url(r'^update/(?P<pk>\d+)$', login_required(views.ProjectUpdateView.as_view()), name='update'),
    url(r'^project/edit/(?P<pk>\d+)/editors$', login_required(views.ProjectEditorUpdateView.as_view()), name='editors'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Project, geometry_field='coordonnees_geographiques', properties=('nom', 'commune', 'description', 'commune_label', 'short_description', 'feature', 'url', 'state')), name='data'),
    url(r'^commune-autocomplete/$', CommuneAutocomplete.as_view(), name='commune-autocomplete'),
    url(r'^editor-autocomplete/$', EditorAutocomplete.as_view(), name='editor-autocomplete'),
]

admin.site.site_header = "ÉcoQuartiers"
