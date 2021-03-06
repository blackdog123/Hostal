# Generated by Django 3.1.7 on 2021-04-17 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alojamiento', '0046_auto_20210416_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='priceroom',
            old_name='tipohabitacion',
            new_name='tipo_habitacion',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='noches',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alojamiento.pricenight'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='personas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alojamiento.pricepeople'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='tipo_habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alojamiento.priceroom'),
        ),
    ]
