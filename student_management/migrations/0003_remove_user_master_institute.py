# Generated by Django 2.1.1 on 2018-09-15 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0002_user_master'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_master',
            name='institute',
        ),
    ]
