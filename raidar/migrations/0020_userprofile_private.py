# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-13 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raidar', '0019_user_email_set_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='private',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
