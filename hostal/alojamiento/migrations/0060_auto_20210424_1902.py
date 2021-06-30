# Generated by Django 3.1.7 on 2021-04-24 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamiento', '0059_auto_20210422_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_producto', models.CharField(blank=True, max_length=80, null=True)),
                ('categoria', models.CharField(blank=True, choices=[('Bebestibles', 'Bebestibles'), ('Carnes', 'Carnes'), ('Lácteos', 'Lácteos'), ('Verduras', 'Verduras'), ('No Perecibles', 'No Perecibles'), ('Otros', 'Otros')], max_length=50, null=True)),
                ('producto', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField(blank=True, max_length=255, null=True)),
                ('precio', models.CharField(blank=True, max_length=50, null=True)),
                ('stock', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo_producto', models.CharField(blank=True, choices=[('Stock Crítico', 'Stock Crítico'), ('No Crítico', 'No Crítico')], max_length=50, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='fecha_creacion',
            new_name='tiempo_transcurrido',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='email',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='noches',
        ),
        migrations.AddField(
            model_name='guest',
            name='fecha_ingreso',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='guest',
            name='fecha_salida',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='estado_ticket',
            field=models.CharField(blank=True, choices=[('Sin pagar', 'Sin pagar'), ('Pagada', 'Pagada'), ('Anulada', 'Anulada')], default='Sin pagar', max_length=50, null=True),
        ),
    ]
