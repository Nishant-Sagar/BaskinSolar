# Generated by Django 4.1.1 on 2022-09-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baskin', '0002_alter_details_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='address',
            field=models.CharField(max_length=300),
        ),
    ]
