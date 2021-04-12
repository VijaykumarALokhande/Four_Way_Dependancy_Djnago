# Generated by Django 2.2.19 on 2021-04-12 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20210412_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='village',
            name='name',
            field=models.CharField(default='karam', max_length=40),
        ),
        migrations.CreateModel(
            name='Gali',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Village')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='gali',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='persons.Gali'),
        ),
    ]
