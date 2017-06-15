# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 06:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20170604_0608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='coupons',
            new_name='user',
        ),
        migrations.AddField(
            model_name='coupon',
            name='coupon',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='coupon',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='date published'),
        ),
    ]
