# Generated by Django 4.2.6 on 2023-10-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legales', '0015_alter_causa_fecha_facturado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='causa',
            name='confesional',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='causa',
            name='testimonial',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
