# Generated by Django 3.2.6 on 2022-07-10 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_good_added_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='type_name',
            new_name='type',
        ),
    ]
