# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chore', '0003_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chore',
            name='complete',
        ),
    ]
