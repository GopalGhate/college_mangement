# Generated by Django 2.1.1 on 2018-09-15 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management.Institute')),
            ],
        ),
    ]