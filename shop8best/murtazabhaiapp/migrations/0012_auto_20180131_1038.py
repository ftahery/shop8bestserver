# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-31 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('murtazabhaiapp', '0011_auto_20180131_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='ordered_item',
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='order_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='murtazabhaiapp.Orders'),
            preserve_default=False,
        ),
    ]
