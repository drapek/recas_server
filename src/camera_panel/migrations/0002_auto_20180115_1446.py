# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-15 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camera_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('datetime', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='camera',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AddField(
            model_name='video',
            name='camera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camera_panel.Camera'),
        ),
    ]
