# Generated by Django 4.2.6 on 2023-11-14 13:36

from django.db import migrations, models
import legales.models


class Migration(migrations.Migration):

    dependencies = [
        ('legales', '0035_delete_oficio'),
    ]

    operations = [
        migrations.AddField(
            model_name='causa',
            name='oficios',
            field=legales.models.ModifiedArrayField(base_field=models.CharField(blank=True, choices=[('AFIP', 'AFIP'), ('CENTRO MEDICO', 'CENTRO MEDICO'), ('CORREO', 'CORREO'), ('EMPLEADOR', 'EMPLEADOR'), ('JUZGADO', 'JUZGADO'), ('SRT', 'SRT'), ('TRIBUNAL', 'TRIBUNAL')], max_length=100, null=True), blank=True, null=True, size=None),
        ),
    ]
