# Generated by Django 4.2.4 on 2023-08-25 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=1024)),
                ('vin', models.CharField(default='', max_length=1024)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
