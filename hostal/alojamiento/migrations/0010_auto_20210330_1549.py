# Generated by Django 3.1.7 on 2021-03-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamiento', '0009_auto_20210330_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cantidad_empleados',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
