# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-03 07:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('murtazabhaiapp', '0013_auto_20180131_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordereditem',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ordereditem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='order_status',
        ),
        migrations.RemoveField(
            model_name='useraddresses',
            name='id',
        ),
        migrations.RemoveField(
            model_name='useraddresses',
            name='user',
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='order_status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='ordered_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordereditem',
            name='user_email',
            field=models.ForeignKey(db_column='user_email', default=1, on_delete=django.db.models.deletion.CASCADE, to='murtazabhaiapp.UserAccount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddresses',
            name='address_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraddresses',
            name='user_email',
            field=models.ForeignKey(db_column='user_email', default=1, on_delete=django.db.models.deletion.CASCADE, to='murtazabhaiapp.UserAccount'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordereditem',
            name='order_id',
            field=models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, to='murtazabhaiapp.Orders'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='delivery_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_address', to='murtazabhaiapp.UserAddresses'),
        ),
    ]
