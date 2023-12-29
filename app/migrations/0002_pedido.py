# Generated by Django 4.2.7 on 2023-11-22 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('direccion_entrega', models.CharField(max_length=255)),
                ('productos', models.ManyToManyField(to='app.producto')),
            ],
        ),
    ]
