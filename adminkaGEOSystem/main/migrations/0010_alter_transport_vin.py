# Generated by Django 4.2.4 on 2023-08-28 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_transport_transport_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='vin',
            field=models.CharField(default='', max_length=1024, null=True, verbose_name='VIN номер'),
        ),
    ]
