# Generated by Django 3.1.7 on 2021-03-27 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamiento', '0002_auto_20210327_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='tipo_cama',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]