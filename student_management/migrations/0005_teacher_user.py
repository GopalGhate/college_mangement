# Generated by Django 2.1.1 on 2018-09-16 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0004_institute_institute_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student_management.User_master'),
            preserve_default=False,
        ),
    ]
