# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('acronym', models.CharField(max_length=30, unique=True)),
                ('country', models.CharField(max_length=30)),
                ('parent', models.ForeignKey(to='team.Institution', blank=True, related_name='children', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30)),
                ('email', models.EmailField(verbose_name='email address', max_length=254)),
                ('institution', models.ForeignKey(to='team.Institution', blank=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, blank=True, related_name='person', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('acronym', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TeamPerson',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('is_coordinator', models.BooleanField()),
                ('person', models.ForeignKey(related_name='team_persons', to='team.Person')),
                ('team', models.ForeignKey(related_name='team_persons', to='team.Team')),
            ],
        ),
    ]
