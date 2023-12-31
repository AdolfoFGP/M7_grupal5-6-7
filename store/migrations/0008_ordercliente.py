# Generated by Django 4.2.3 on 2023-09-05 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_precio_order_total_alter_order_direccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(default='hola.adadis@outlook.com', max_length=50)),
                ('direccion', models.CharField(default='En Sucursal', max_length=100)),
                ('cantidad', models.IntegerField(null=True)),
                ('metodo_pago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Debito', 'Debito'), ('Credito', 'Credito')], default='Efectivo')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
