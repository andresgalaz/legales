# Generated by Django 4.2.6 on 2023-10-26 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legales', '0011_alter_causa_monto_demanda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causa',
            name='monto_bono',
            field=models.DecimalField(decimal_places=2, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='causa',
            name='monto_jus',
            field=models.DecimalField(decimal_places=2, max_digits=14, null=True),
        ),
    ]