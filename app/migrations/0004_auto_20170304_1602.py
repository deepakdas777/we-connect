# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='item',
        ),
    ]
