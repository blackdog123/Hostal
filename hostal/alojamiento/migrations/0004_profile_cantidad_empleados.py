# Generated by Django 3.1.7 on 2021-03-27 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamiento', '0003_auto_20210327_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cantidad_empleados',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
