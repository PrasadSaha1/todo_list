# Generated by Django 5.1.1 on 2024-09-21 14:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PomodoroTimer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('work_period', models.FloatField()),
                ('break_period', models.FloatField()),
                ('times_repeat', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pomodoroTimer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
