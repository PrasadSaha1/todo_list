# Generated by Django 5.1.1 on 2024-09-22 14:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_pomodorotimer_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pomodorotimer',
            name='break_period',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pomodorotimer',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pomodorotimer',
            name='work_period',
            field=models.IntegerField(),
        ),
    ]
