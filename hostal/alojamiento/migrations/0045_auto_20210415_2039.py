# Generated by Django 3.1.7 on 2021-04-16 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamiento', '0044_auto_20210415_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proovider',
            name='codigo_proveedor',
        ),
        migrations.AddField(
            model_name='proovider',
            name='telefono',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
