# Generated by Django 3.1.7 on 2021-05-29 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamiento', '0071_auto_20210529_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='precio_servivcio',
        ),
        migrations.AddField(
            model_name='ticket',
            name='precio_servicio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='cargo',
            field=models.CharField(choices=[('Sin Cargo', 'Sin Cargo'), ('Administrador', 'Administrador'), ('Ayudante Cocina', 'Ayudante Cocina'), ('Recepcionista', 'Recepcionista'), ('Solicitante', 'Solicitante')], default='Sin Cargo', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='cantidad',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='estado',
            field=models.CharField(choices=[('En Proceso', 'En Proceso'), ('Despachado', 'Despachado'), ('En Camino', 'En Camino'), ('Recibida', 'Recibida'), ('Rechazada', 'Rechazada')], default='En Proceso', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='producto',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='cantidad_dias',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='estado_ticket',
            field=models.CharField(choices=[('Sin pagar', 'Sin pagar'), ('Pagada', 'Pagada'), ('Anulada', 'Anulada')], default='Sin pagar', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='fecha_boleta',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='iva',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='precio_dias',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='subtotal',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='total',
            field=models.CharField(max_length=50, null=True),
        ),
    ]