# Generated by Django 4.2.6 on 2023-10-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legales', '0019_alter_causa_fecha_presentacion_acuerdo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causa',
            name='hay_cbu',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='causa',
            name='homologado',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
