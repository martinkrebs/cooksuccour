# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20160523_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='#First ingredient.\n#Second ingredient.'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default='#1 First instruction\n#2 Second instruction. (fig. A)'),
        ),
    ]
