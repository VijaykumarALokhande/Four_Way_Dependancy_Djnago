# Generated by Django 2.2.19 on 2021-04-12 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0004_auto_20210412_1059'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='City',
            new_name='State',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='city',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='village',
            old_name='city',
            new_name='state',
        ),
    ]
