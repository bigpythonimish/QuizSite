# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 09:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
    ]
