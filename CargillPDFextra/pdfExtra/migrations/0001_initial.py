# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-11 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PdfExtraModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=125, null=True)),
                ('file', models.FileField(upload_to='')),
                ('format', models.CharField(max_length=125, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('result', models.TextField(null=True)),
            ],
        ),
    ]
