# Generated by Django 4.1.7 on 2023-05-30 13:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0010_alter_askquestion_time_alter_members_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askquestion',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 19, 17, 59, 856657)),
        ),
        migrations.AlterField(
            model_name='members',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='group.group'),
        ),
    ]
