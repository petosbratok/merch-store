# Generated by Django 3.2.6 on 2022-07-10 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_added_date_good_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='photo',
            field=models.ImageField(default='изображение_2022-07-10_235015707', upload_to='merch_pics'),
        ),
    ]
