# Generated by Django 4.2.6 on 2023-10-26 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legales', '0023_alter_causa_estado_negociacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causa',
            name='porcentaje_srt',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
