# Generated by Django 4.1.7 on 2023-06-02 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_profile_paid_remove_profile_paid_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='reveal',
        ),
    ]
