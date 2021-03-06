# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-16 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('camera_panel', '0003_auto_20180115_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='CameraIntegerSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('setting_variable_name', models.CharField(max_length=256)),
                ('value', models.IntegerField()),
                ('min_value', models.IntegerField()),
                ('max_value', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=256)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camera_panel.Camera')),
            ],
        ),
    ]
