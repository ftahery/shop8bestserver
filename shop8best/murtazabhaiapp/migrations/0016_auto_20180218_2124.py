# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-18 21:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('murtazabhaiapp', '0015_auto_20180209_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditem',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='murtazabhaiapp.Items'),
        ),
    ]