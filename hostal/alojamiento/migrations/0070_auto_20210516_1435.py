# Generated by Django 3.1.7 on 2021-05-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamiento', '0069_auto_20210516_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='texto',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='texto',
            field=models.TextField(),
        ),
    ]