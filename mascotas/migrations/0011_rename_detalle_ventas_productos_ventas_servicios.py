# Generated by Django 4.0 on 2021-12-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0010_detalles_servicio_alter_ventas_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ventas',
            old_name='detalle',
            new_name='productos',
        ),
        migrations.AddField(
            model_name='ventas',
            name='servicios',
            field=models.ManyToManyField(blank=True, through='mascotas.Detalles', to='mascotas.Servicios'),
        ),
    ]
