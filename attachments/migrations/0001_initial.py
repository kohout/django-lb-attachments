# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import attachments.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(max_length=255, upload_to=attachments.models.upload_attachment_file_path)),
                ('org_filename', models.TextField()),
                ('suffix', models.CharField(default=b'', max_length=8, blank=True)),
                ('is_img', models.BooleanField(default=False)),
                ('num_downloads', models.IntegerField(default=0)),
                ('description', models.TextField(default=b'', blank=True)),
                ('activated', models.BooleanField(default=False)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(verbose_name='Attachment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
