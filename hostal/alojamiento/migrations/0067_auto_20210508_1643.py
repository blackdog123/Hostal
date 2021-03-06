# Generated by Django 3.1.7 on 2021-05-08 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alojamiento', '0066_auto_20210508_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='alojamiento.proovider'),
        ),
        migrations.AlterField(
            model_name='proovider',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
