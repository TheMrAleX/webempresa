# Generated by Django 4.2.15 on 2024-09-16 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 16, 16, 6, 32, 217941, tzinfo=datetime.timezone.utc), verbose_name='Fecha de publicación'),
        ),
    ]
