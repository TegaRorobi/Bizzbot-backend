# Generated by Django 4.2.2 on 2023-11-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_owner_product_seller_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='delivery_time',
            field=models.DurationField(default=None),
            preserve_default=False,
        ),
    ]
