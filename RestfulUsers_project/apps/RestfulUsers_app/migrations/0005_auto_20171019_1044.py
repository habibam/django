# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestfulUsers_app', '0004_auto_20171019_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='last_name', max_length=255),
            preserve_default=False,
        ),
    ]