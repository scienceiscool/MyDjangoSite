# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fortune',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('filename', models.CharField(max_length=16)),
                ('size', models.IntegerField()),
                ('aphorism', models.CharField(max_length=2147)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
