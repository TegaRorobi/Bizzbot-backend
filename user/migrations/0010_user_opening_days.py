# Generated by Django 4.2.2 on 2023-11-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_openingday_day'),
        ('user', '0009_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='opening_days',
            field=models.ManyToManyField(to='api.openingday', verbose_name='Opening Days'),
        ),
    ]
