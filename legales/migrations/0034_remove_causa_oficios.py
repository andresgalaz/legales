# Generated by Django 4.2.6 on 2023-11-14 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legales', '0033_alter_causa_contra_oferta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='causa',
            name='oficios',
        ),
    ]
