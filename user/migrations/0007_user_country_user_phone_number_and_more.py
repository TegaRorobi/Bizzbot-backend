# Generated by Django 4.2.2 on 2023-11-17 10:49

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_business_description_user_business_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='business_description',
            field=models.TextField(blank=True, null=True, verbose_name='Business Description'),
        ),
    ]
