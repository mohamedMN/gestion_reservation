# Generated by Django 4.0.4 on 2022-05-27 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_utilisateur_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='avatar',
            field=models.ImageField(blank=True, default='profile.png', upload_to=''),
        ),
    ]
