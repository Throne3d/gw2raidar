# Generated by Django 2.0.4 on 2018-05-15 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raidar', '0039_merge_20180318_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='eraareastore',
            name='leaderboards_value',
            field=models.TextField(default='{}', editable=False),
        ),
    ]
