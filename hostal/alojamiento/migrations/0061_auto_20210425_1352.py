# Generated by Django 3.1.7 on 2021-04-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alojamiento', '0060_auto_20210424_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categoria',
            field=models.CharField(choices=[('Bebestibles', 'Bebestibles'), ('Carnes', 'Carnes'), ('Congelados', 'Congelados'), ('Lácteos', 'Lácteos'), ('Pastas', 'Pastas'), ('Verduras', 'Verduras'), ('No Perecibles', 'No Perecibles'), ('Otros', 'Otros')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='codigo_producto',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='precio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='producto',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tipo_producto',
            field=models.CharField(choices=[('Stock Crítico', 'Stock Crítico'), ('No Crítico', 'No Crítico')], max_length=50, null=True),
        ),
    ]