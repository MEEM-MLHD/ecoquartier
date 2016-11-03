# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-03 16:06
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command


def loadfixture(apps, schema_editor):
    call_command('loaddata', 'initial_data.json')


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0091_document_engagement'),
    ]

    operations = [
    	migrations.RunPython(loadfixture),
    ]