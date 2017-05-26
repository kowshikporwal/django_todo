# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-20 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20170320_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='No_Label', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Label'),
        ),
    ]
