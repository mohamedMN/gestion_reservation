# Generated by Django 4.0.4 on 2022-05-31 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_remove_salle_nbdispo_remove_salle_nbocc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='date_enter',
            new_name='check_in',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='date_sortir',
            new_name='check_out',
        ),
        migrations.AlterField(
            model_name='salle',
            name='nom',
            field=models.CharField(choices=[('doctorant', 'doctorant')], default='doctorant', max_length=190, null=True),
        ),
    ]
