# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(verbose_name='By user')),
                ('order_date', models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Order date')),
                ('amount', models.PositiveIntegerField()),
                ('is_paid', models.BooleanField(default=False, verbose_name='Has been paid')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
