# Generated by Django 4.2.6 on 2023-10-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legales', '0020_alter_causa_hay_cbu_alter_causa_homologado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causa',
            name='fecha_asigno_pmp',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='causa',
            name='fecha_pedido_pmp',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='causa',
            name='fecha_pmp',
            field=models.DateField(null=True),
        ),
    ]
