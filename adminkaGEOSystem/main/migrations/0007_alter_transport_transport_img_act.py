# Generated by Django 4.2.4 on 2023-08-28 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_transport_transport_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='transport_img',
            field=models.ImageField(upload_to=''),
        ),
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('executor', models.CharField(default='', max_length=1024)),
                ('description', models.CharField(default='', max_length=1024)),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.transport')),
            ],
        ),
    ]
