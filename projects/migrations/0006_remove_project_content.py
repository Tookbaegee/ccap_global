# Generated by Django 3.0.6 on 2020-06-13 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200613_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='content',
        ),
    ]
