# Generated by Django 4.0.4 on 2022-05-29 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_utilisateur_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='avatar',
            field=models.ImageField(default='static/images/profile.png', upload_to='images'),
        ),
    ]
