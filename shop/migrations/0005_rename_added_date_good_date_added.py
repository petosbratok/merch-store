# Generated by Django 3.2.6 on 2022-07-10 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_type_name_type_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='added_date',
            new_name='date_added',
        ),
    ]