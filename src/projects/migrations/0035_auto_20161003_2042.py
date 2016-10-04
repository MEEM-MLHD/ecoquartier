# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-03 20:42
from __future__ import unicode_literals

from django.db import migrations


def change_absent(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    projects = Project.objects.all()
    for project in projects:
        if project.eau == 'ABSENT':
            project.eau = ''
        if project.dechets == 'ABSENT':
            project.dechets = ''
        if project.biodiversite == 'ABSENT':
            project.biodiversite = ''
        if project.mobilite == 'ABSENT':
            project.mobilite = ''
        if project.sobriete_energetique_et_energie_renouvelable == 'ABSENT':
            project.sobriete_energetique_et_energie_renouvelable = ''
        if project.densite_et_formes_urbaines == 'ABSENT':
            project.densite_et_formes_urbaines = ''
        if project.ecoconstruction == 'ABSENT':
            project.ecoconstruction = ''
        if project.autres == 'ABSENT':
            project.autres = ''
        if project.demarches_et_processus == 'ABSENT':
            project.demarches_et_processus = ''
        if project.cadre_de_vie_et_usages == 'ABSENT':
            project.cadre_de_vie_et_usages = ''
        project.save()


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0034_auto_20161003_2031'),
    ]

    operations = [
        migrations.RunPython(change_absent, reverse_func),
    ]