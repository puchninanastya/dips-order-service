# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 00:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order_service', '0003_ordercourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Order datetime'),
        ),
    ]