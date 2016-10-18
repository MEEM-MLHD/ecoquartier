# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-18 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0079_auto_20161018_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Echelle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='echelle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Echelle'),
        ),
    ]
