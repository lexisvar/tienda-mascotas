# Generated by Django 4.0 on 2021-12-10 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0003_clientesmascotas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('total', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mascotas.productos')),
                ('id_servicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mascotas.servicios')),
            ],
            options={
                'db_table': 'ventas',
            },
        ),
    ]