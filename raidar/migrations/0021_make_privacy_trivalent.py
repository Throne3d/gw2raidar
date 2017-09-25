# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-13 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raidar', '0020_userprofile_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='private',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='privacy',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Private'), (2, 'Squad'), (3, 'Public')], default=3, editable=False),
        ),
    ]
