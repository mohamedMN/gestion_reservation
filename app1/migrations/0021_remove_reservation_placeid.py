# Generated by Django 4.0.4 on 2022-06-02 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_remove_reservation_id_remove_reservation_placeid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='placeID',
        ),
    ]
