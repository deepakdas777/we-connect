# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 08:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_unlike'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_logo',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_name',
            new_name='post',
        ),
    ]