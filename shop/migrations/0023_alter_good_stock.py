# Generated by Django 3.2.6 on 2022-07-18 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_auto_20220718_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='stock',
            field=models.CharField(default='xs_100;s_100;m_100;l_100;xl_100', max_length=100),
        ),
    ]
