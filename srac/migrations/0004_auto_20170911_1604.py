# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 08:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('srac', '0003_auto_20170907_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location_Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_number', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
                ('check_date', models.DateTimeField()),
                ('check_remarks', models.TextField()),
                ('is_session_submitted', models.IntegerField(default=0)),
                ('checker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session_Checklist',
            fields=[
                ('session_checklist_id', models.AutoField(primary_key=True, serialize=False)),
                ('confirmation', models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('NA', 'Not Applicable')], max_length=45)),
                ('remarks', models.TextField()),
                ('location_checklist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srac.Location_Checklist')),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srac.Session')),
            ],
        ),
        migrations.RemoveField(
            model_name='check_item_log',
            name='check_session_id',
        ),
        migrations.RemoveField(
            model_name='check_item_log',
            name='checklist_id',
        ),
        migrations.RemoveField(
            model_name='check_session_log',
            name='checker',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='location_hash',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='priority_number',
        ),
        migrations.DeleteModel(
            name='Check_Item_Log',
        ),
        migrations.DeleteModel(
            name='Check_Session_Log',
        ),
        migrations.AddField(
            model_name='location_checklist',
            name='checklist_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srac.Checklist'),
        ),
        migrations.AddField(
            model_name='location_checklist',
            name='location_hash',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srac.Location'),
        ),
    ]
