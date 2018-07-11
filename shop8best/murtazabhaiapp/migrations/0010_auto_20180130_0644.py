# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-30 06:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('murtazabhaiapp', '0009_auto_20180127_0945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddresses',
            old_name='user_address',
            new_name='user_name',
        ),
        migrations.AddField(
            model_name='useraddresses',
            name='user_area',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddresses',
            name='user_building_details',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddresses',
            name='user_contact_number',
            field=models.CharField(default=1, max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+96565624892 or 65624892'. Up to 12 digits allowed", regex='^\\+?1?\\d{8,12}$')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddresses',
            name='user_country',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddresses',
            name='user_pincode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddresses',
            name='user_street_details',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='murtazabhaiapp.Items'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user_contact_number',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+96565624892'. Up to 12 digits allowed", regex='^\\+?1?\\d{8,12}$')]),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='user_contact_number',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+96565624892'. Up to 12 digits allowed", regex='^\\+?1?\\d{8,12}$')]),
        ),
    ]