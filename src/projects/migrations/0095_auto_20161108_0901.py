# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-08 09:01
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command


def loadfixture(apps, schema_editor):
    call_command('loaddata', 'data2.json')


def backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0094_auto_20161107_2125'),
    ]

    operations = [
        migrations.RunPython(loadfixture, backward),
    ]
