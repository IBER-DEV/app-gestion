# Generated by Django 5.1.5 on 2025-01-31 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('contacto', models.CharField(max_length=50)),
                ('observaciones', models.TextField()),
            ],
        ),
    ]
