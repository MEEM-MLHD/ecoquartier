# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-18 10:06
from __future__ import unicode_literals

from django.db import migrations


def forward(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Demarche = apps.get_model("projects", "Demarche")
    AEU, created = Demarche.objects.get_or_create(label='AEU')
    HQE, created = Demarche.objects.get_or_create(label='HQE')
    Agenda21, created = Demarche.objects.get_or_create(label='Agenda21')
    Ecocite, created = Demarche.objects.get_or_create(label=u'Ecocité')
    projects = Project.objects.all()

    ps = projects.filter(label_demarche__icontains='AEU')
    for p in ps:
        p.demarches.add(AEU)

    ps = projects.filter(label_demarche__icontains='HQE')
    for p in ps:
        p.demarches.add(HQE)

    ps = projects.filter(label_demarche__icontains='Agenda21')
    for p in ps:
        p.demarches.add(Agenda21)

    ps = projects.filter(label_demarche__icontains=u'Ecocité')
    for p in ps:
        p.demarches.add(Ecocite)


def backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0078_auto_20161018_1006'),
    ]

    operations = [
        migrations.RunPython(forward, backward),
    ]
