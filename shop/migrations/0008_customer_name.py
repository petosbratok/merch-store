# Generated by Django 3.2.6 on 2022-07-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_customer_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
