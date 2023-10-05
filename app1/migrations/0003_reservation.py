# Generated by Django 4.0.4 on 2022-05-20 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.CharField(choices=[('accepter', 'accepter'), ('reject', 'reject')], max_length=190, null=True)),
            ],
        ),
    ]
