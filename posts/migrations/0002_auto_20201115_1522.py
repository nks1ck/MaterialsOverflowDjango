# Generated by Django 3.1.3 on 2020-11-15 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='language',
            new_name='languages',
        ),
    ]
