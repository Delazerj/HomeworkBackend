# Generated by Django 2.2.6 on 2019-11-10 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomeworkBackend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='country',
            new_name='name',
        ),
    ]
