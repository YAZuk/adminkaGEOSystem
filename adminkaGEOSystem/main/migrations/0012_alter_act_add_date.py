# Generated by Django 4.2.4 on 2023-08-28 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_act_add_date_alter_transport_transport_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='add_date',
            field=models.DateTimeField(verbose_name='Дата и время создания'),
        ),
    ]
