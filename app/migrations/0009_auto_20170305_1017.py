# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 04:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170305_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_details',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_price',
        ),
    ]
