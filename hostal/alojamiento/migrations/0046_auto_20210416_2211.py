# Generated by Django 3.1.7 on 2021-04-17 02:11

import alojamiento.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamiento', '0045_auto_20210415_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceNight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_noches', models.CharField(blank=True, max_length=255, null=True)),
                ('precio', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PricePeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_peronas', models.CharField(blank=True, max_length=255, null=True)),
                ('precio', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipohabitacion', models.CharField(blank=True, max_length=255, null=True)),
                ('precio', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Estate',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.RenameField(
            model_name='booking_client',
            old_name='lista_personas',
            new_name='mensaje',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='precio_noches',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='precio_personas',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='precio_servivcio',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='fecha_boleta',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='noches',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=alojamiento.models.PriceNight),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='personas',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=alojamiento.models.PricePeople),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='tipo_habitacion',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=alojamiento.models.PriceRoom),
        ),
    ]
