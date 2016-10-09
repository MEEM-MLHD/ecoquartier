# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-08 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0063_auto_20161007_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='DDTStringer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Departement')),
            ],
        ),
        migrations.CreateModel(
            name='DREALStringer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='drealstringer',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Person'),
        ),
        migrations.AddField(
            model_name='drealstringer',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Region'),
        ),
        migrations.AddField(
            model_name='ddtstringer',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Person'),
        ),
        migrations.AddField(
            model_name='departement',
            name='stringers',
            field=models.ManyToManyField(through='projects.DDTStringer', to='projects.Person'),
        ),
        migrations.AddField(
            model_name='region',
            name='stringers',
            field=models.ManyToManyField(through='projects.DREALStringer', to='projects.Person'),
        ),
    ]