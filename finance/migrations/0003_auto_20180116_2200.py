# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20180116_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminapply',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='./upload/attachment/', verbose_name='上传附件'),
        ),
        migrations.AddField(
            model_name='adminapply',
            name='note',
            field=models.CharField(max_length=64, null=True, verbose_name='备注'),
        ),
    ]