# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-05 16:08
from __future__ import unicode_literals

from django.db import migrations


def oui_non(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    projects = Project.objects.all()
    for project in projects:
        if project.participation_2009 == 'OUI':
            project.participation_2009 = 1
        else:
            project.participation_2009 = 0

        if project.participation_2011 == 'OUI':
            project.participation_2011 = 1
        else:
            project.participation_2011 = 0

        if project.nomine == 'OUI':
            project.nomine = 1
        else:
            project.nomine = 0

        if project.laureat == 'OUI':
            project.laureat = 1
        else:
            project.laureat = 0

        project.save()


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0052_auto_20161005_1551'),
    ]

    operations = [
        migrations.RunPython(oui_non, reverse_func),
    ]
