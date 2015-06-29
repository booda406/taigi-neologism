# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChineseWords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, help_text='', auto_created=True)),
                ('word', models.CharField(max_length=168, help_text='')),
                ('pronounce', models.CharField(max_length=168, help_text='')),
                ('created_at', models.DateTimeField(help_text='', auto_now_add=True)),
            ],
        ),
    ]
