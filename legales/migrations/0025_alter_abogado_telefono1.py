# Generated by Django 4.2.6 on 2023-10-26 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legales', '0024_alter_causa_porcentaje_srt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abogado',
            name='telefono1',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
