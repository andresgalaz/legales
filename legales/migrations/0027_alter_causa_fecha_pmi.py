# Generated by Django 4.2.6 on 2023-10-26 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legales', '0026_remove_causa_excepcion_excepcioncausa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causa',
            name='fecha_pmi',
            field=models.DateField(null=True),
        ),
    ]