# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 21:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare_profile', '0002_auto_20160503_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='car_brand',
            new_name='carbrand',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='car_seat',
            new_name='carseat',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='pets_allowed',
            new_name='petsallowed',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='phone_number',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='point',
            new_name='start_point',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='in_profile',
            new_name='user',
        ),
    ]
