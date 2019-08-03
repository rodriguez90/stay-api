# Generated by Django 2.2.3 on 2019-08-03 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedure_resource', '0004_auto_20190731_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='personprocedurestep',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='personprocedurestepdocument',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='personprocedurestepdocument',
            name='status',
            field=models.CharField(choices=[(1, 'Pendiente'), (3, 'Rechazado'), (4, 'Aceptado')], default=1, max_length=2),
        ),
    ]
