# Generated by Django 4.1.7 on 2023-05-24 10:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_profile_last_login'),
        ('group', '0008_alter_askquestion_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askquestion',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 16, 14, 50, 496201)),
        ),
        migrations.AlterField(
            model_name='group',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.profile'),
        ),
    ]