# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='last_visit',
            field=models.DateTimeField(null=True),
        ),
    ]
