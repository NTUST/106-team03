# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 06:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0002_data_follows'),
    ]

    operations = [
        migrations.CreateModel(
            name='coupons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='data',
            name='follows',
        ),
        migrations.RemoveField(
            model_name='data',
            name='user',
        ),
        migrations.DeleteModel(
            name='data',
        ),
    ]
