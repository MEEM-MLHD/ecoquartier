# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-05 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0057_auto_20161005_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='collectivite_ou_epci_porteur',
            field=models.CharField(max_length=500),
        ),
    ]
