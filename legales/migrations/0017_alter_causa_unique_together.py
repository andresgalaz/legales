# Generated by Django 4.2.6 on 2023-10-26 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legales', '0016_alter_causa_confesional_alter_causa_testimonial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='causa',
            unique_together={('asunto',)},
        ),
    ]
