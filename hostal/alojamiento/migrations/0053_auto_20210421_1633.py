# Generated by Django 3.1.7 on 2021-04-21 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamiento', '0052_auto_20210420_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking_client',
            old_name='fecha',
            new_name='fecha_llegada',
        ),
        migrations.RemoveField(
            model_name='booking_client',
            name='noches',
        ),
        migrations.RemoveField(
            model_name='booking_client',
            name='personas',
        ),
        migrations.AddField(
            model_name='booking_client',
            name='apellido',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='booking_client',
            name='apellido2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='booking_client',
            name='cantidad_camas',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='booking_client',
            name='fecha_salida',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking_client',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='booking_client',
            name='nombre2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='booking_client',
            name='numero_habitacion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='booking_client',
            name='rut',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='booking_client',
            name='rut2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='booking_client',
            name='tipo_cama',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='booking_client',
            name='tipo_habitacion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='imagen_habitacion',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to='habitaciones'),
        ),
    ]
