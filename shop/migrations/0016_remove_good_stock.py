# Generated by Django 3.2.6 on 2022-07-16 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_good_stock_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='stock',
        ),
    ]