# Generated by Django 3.2.6 on 2022-07-16 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_order_delivery_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.deliveryinfo'),
        ),
    ]