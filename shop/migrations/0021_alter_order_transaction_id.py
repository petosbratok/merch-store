# Generated by Django 3.2.6 on 2022-07-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default=9999999999999999, max_length=100),
        ),
    ]
