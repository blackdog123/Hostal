# Generated by Django 3.1.7 on 2021-03-28 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alojamiento', '0005_auto_20210328_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='ubicacion',
            new_name='sede',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='ubicacion',
            new_name='sede',
        ),
    ]