# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('topic', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('publish_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='source',
            field=models.ForeignKey(to='feeds.Source'),
        ),
        migrations.AddField(
            model_name='article',
            name='board',
            field=models.ForeignKey(to='feeds.Board'),
        ),
        migrations.AddField(
            model_name='article',
            name='source',
            field=models.ForeignKey(to='feeds.Source'),
        ),
    ]
