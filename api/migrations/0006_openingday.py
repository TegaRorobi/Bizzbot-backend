# Generated by Django 4.2.2 on 2023-11-18 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_product_delivery_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('day', models.CharField(max_length=20, verbose_name='Day of the Week')),
                ('opening_time', models.TimeField(verbose_name='Opening Time')),
                ('closing_time', models.TimeField(verbose_name='Closing Time')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]