# Generated by Django 4.2.6 on 2023-10-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legales', '0013_alter_causa_preexistencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causa',
            name='contra_oferta',
            field=models.DecimalField(decimal_places=2, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='causa',
            name='fecha_ultimo_ofrecimiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='causa',
            name='monto_acuerdo',
            field=models.DecimalField(decimal_places=2, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='causa',
            name='monto_autorizado',
            field=models.DecimalField(decimal_places=2, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='causa',
            name='ofrecimiento',
            field=models.DecimalField(decimal_places=2, max_digits=14, null=True),
        ),
    ]
