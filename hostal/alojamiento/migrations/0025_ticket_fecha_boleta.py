# Generated by Django 3.1.7 on 2021-04-05 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamiento', '0024_auto_20210404_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='fecha_boleta',
            field=models.DateField(blank=True, null=True),
        ),
    ]
