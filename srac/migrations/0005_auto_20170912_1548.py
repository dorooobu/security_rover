# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 07:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srac', '0004_auto_20170911_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='classification_name',
            new_name='classification',
        ),
        migrations.RenameField(
            model_name='location_checklist',
            old_name='checklist_id',
            new_name='checklist',
        ),
        migrations.RenameField(
            model_name='location_checklist',
            old_name='location_hash',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='session_checklist',
            old_name='location_checklist_id',
            new_name='location_checklist',
        ),
        migrations.RenameField(
            model_name='session_checklist',
            old_name='session_id',
            new_name='session',
        ),
    ]