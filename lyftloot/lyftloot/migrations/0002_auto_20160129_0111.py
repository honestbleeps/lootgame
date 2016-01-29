# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lyftloot', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='useranswer',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='question',
        ),
    ]
