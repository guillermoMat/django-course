# Generated by Django 5.1 on 2024-08-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, verbose_name='Nombre')),
                ('age', models.IntegerField(verbose_name='Edad')),
                ('birthday', models.DateField(verbose_name='Nacimiento')),
                ('isAdmin', models.BooleanField(default=False, verbose_name='Permiso de administrador')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('page', models.URLField(null=True, verbose_name='Página web')),
            ],
        ),
    ]
