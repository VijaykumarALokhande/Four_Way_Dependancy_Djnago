# Generated by Django 2.2.19 on 2021-04-12 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20210411_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default='bangal', max_length=40),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(default='ind', max_length=40),
        ),
    ]
