# Generated by Django 4.0.4 on 2022-06-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_alter_reservation_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]