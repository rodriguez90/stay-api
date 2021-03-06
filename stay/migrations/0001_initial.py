# Generated by Django 2.2.3 on 2019-10-03 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
                ('second_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='segundo nombre')),
                ('second_last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='segundo apellido')),
                ('identification', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='identificación')),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Teléfono')),
                ('address', models.TextField(blank=True, null=True, verbose_name='dirección')),
                ('is_active', models.BooleanField(default=True, verbose_name='esta activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creado el')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='actualizdo el')),
            ],
            options={
                'verbose_name': 'persona',
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('description', models.TextField(verbose_name='descripción')),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('price', models.FloatField(verbose_name='precio')),
                ('phone', models.CharField(max_length=255, verbose_name='teléfono')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('direccion', models.CharField(max_length=255, verbose_name='dirección')),
                ('image', models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='imagen')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('css_icon', models.CharField(max_length=255, verbose_name='icono')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RentService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stay.Rent')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stay.Service')),
            ],
        ),
        migrations.CreateModel(
            name='RentImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='imagen')),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='stay.Rent')),
            ],
        ),
        migrations.AddField(
            model_name='rent',
            name='services',
            field=models.ManyToManyField(related_name='services', through='stay.RentService', to='stay.Service', verbose_name='services'),
        ),
        migrations.AddField(
            model_name='rent',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
