# Generated by Django 4.0.4 on 2022-06-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_alter_reservation_check_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='numero',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]