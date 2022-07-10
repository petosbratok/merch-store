# Generated by Django 3.2.6 on 2022-07-10 20:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(default='no type', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='clothing item', max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='post_pics')),
                ('price', models.DecimalField(decimal_places=2, default=30.0, max_digits=10)),
                ('stock', models.IntegerField(default=1000)),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.type')),
            ],
        ),
    ]
