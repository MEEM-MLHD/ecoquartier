# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-27 19:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20160922_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('title', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d', max_length=1500)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]