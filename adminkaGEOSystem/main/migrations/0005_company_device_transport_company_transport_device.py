# Generated by Django 4.2.4 on 2023-08-28 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_transport_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=1024)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Компания',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imei', models.CharField(default='', max_length=1024)),
                ('name', models.CharField(default='', max_length=1024)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Устройство',
            },
        ),
        migrations.AddField(
            model_name='transport',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transport',
            name='device',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.device'),
            preserve_default=False,
        ),
    ]
