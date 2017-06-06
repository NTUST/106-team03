# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 14:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0019_auto_20170605_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcfollowing',
            name='target',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
