# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 01:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_evento'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Palestrantes',
            new_name='Sobre',
        ),
        migrations.RenameField(
            model_name='palestras',
            old_name='foto_palestra',
            new_name='foto_palestrante',
        ),
        migrations.RenameField(
            model_name='palestras',
            old_name='nome_palestra',
            new_name='nome_palestrante',
        ),
        migrations.RenameField(
            model_name='palestras',
            old_name='apresentacao_palestra',
            new_name='sua_palestra',
        ),
    ]