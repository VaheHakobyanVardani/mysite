# Generated by Django 3.0.5 on 2021-01-25 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210126_0105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='news',
            new_name='views',
        ),
    ]