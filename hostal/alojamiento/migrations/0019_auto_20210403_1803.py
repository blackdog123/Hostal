# Generated by Django 3.1.7 on 2021-04-03 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alojamiento', '0018_remove_employee_foto_empleado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='foto_habitacion',
        ),
        migrations.AddField(
            model_name='room',
            name='tipo_habitacion',
            field=models.CharField(blank=True, choices=[('Básico', 'Básico'), ('Plus', 'Plus'), ('Premuim', 'Plus')], max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Booking_Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('tipo_habitacion', models.CharField(blank=True, choices=[('Básico', 'Básico'), ('Plus', 'Plus'), ('Premuim', 'Plus')], max_length=50, null=True)),
                ('noches', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=50, null=True)),
                ('personas', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=50, null=True)),
                ('lista_personas', models.TextField()),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
