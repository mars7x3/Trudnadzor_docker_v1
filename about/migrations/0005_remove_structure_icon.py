# Generated by Django 4.0.4 on 2022-05-13 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_management_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='structure',
            name='icon',
        ),
    ]
