# Generated by Django 3.0.6 on 2020-06-13 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200610_1123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='front_page',
            new_name='featured',
        ),
    ]
