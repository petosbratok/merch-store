# Generated by Django 3.2.6 on 2022-07-10 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='added_date',
        ),
    ]
