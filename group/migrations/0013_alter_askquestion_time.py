# Generated by Django 4.1.7 on 2023-05-30 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0012_alter_askquestion_time_alter_members_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askquestion',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 22, 9, 42, 613954)),
        ),
    ]
