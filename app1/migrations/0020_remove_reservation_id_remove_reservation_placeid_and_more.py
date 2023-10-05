# Generated by Django 4.0.4 on 2022-06-02 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_rename_date_enter_reservation_check_in_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='id',
        ),
        migrations.AddField(
            model_name='reservation',
            name='place',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app1.place'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='check_in',
            field=models.DateTimeField(),
        ),
        migrations.AddField(
            model_name='reservation',
            name='check_out',
            field=models.DateTimeField(),
        ),
    ]