# Generated by Django 4.2.6 on 2023-10-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legales', '0009_rename_esatdo_negociacion_causa_estado_negociacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causa',
            name='incapacidad_reclamada',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
