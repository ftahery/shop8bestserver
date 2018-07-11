# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-19 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('murtazabhaiapp', '0016_auto_20180218_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_type',
            field=models.CharField(choices=[('ring', 'RING'), ('bracelet', 'BRACELET'), ('necklace', 'NECKLACE')], default='bracelet', max_length=10),
        ),
    ]