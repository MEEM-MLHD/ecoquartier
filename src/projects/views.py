from django.shortcuts import render

from .models import Project
from .filters import ProjectFilter


def home(request):
    f = ProjectFilter(request.GET, queryset=Project.objects.all())
    return render(request, 'home.html', {
        'filter': f
    })