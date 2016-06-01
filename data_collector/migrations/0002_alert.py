# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_collector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('data_type', models.CharField(max_length=100)),
                ('min_value', models.FloatField(null=True, blank=True)),
                ('max_value', models.FloatField(null=True, blank=True)),
                ('node_name', models.CharField(blank=True, max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
