# Generated by Django 4.2.4 on 2023-08-28 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_act_options_alter_company_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='transport_img',
            field=models.ImageField(default='', upload_to='', verbose_name='Изображение'),
        ),
    ]
