# Generated by Django 4.0 on 2021-12-10 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0006_clientes_telefono_mascotas_cliente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascotas',
            name='amo',
        ),
        migrations.RemoveField(
            model_name='mascotas',
            name='amo_telefono',
        ),
    ]
