# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('node_name', models.CharField(max_length=250)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('data_type', models.CharField(max_length=100)),
                ('data_value', models.FloatField()),
            ],
        ),
    ]
