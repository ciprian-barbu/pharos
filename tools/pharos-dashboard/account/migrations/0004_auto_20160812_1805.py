# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userprofile_registration_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gpgkey',
            field=models.CharField(default='a', max_length=2048),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sshkey',
            field=models.CharField(max_length=2048),
        ),
    ]
