# Generated by Django 4.2.4 on 2023-08-28 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_transport_название_transport_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='name',
            field=models.CharField(default='', max_length=1024),
        ),
    ]
