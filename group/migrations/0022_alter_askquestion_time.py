# Generated by Django 4.1.7 on 2023-06-07 15:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0021_alter_askquestion_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askquestion',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]