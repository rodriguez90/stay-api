# Generated by Django 2.2.3 on 2019-08-12 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedure_resource', '0002_auto_20190812_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirement',
            name='position',
            field=models.PositiveIntegerField(verbose_name='orden'),
        ),
    ]