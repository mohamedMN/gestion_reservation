# Generated by Django 4.0.4 on 2022-05-30 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_alter_utilisateur_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='nom',
            new_name='name',
        ),
    ]
