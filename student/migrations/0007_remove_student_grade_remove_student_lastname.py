# Generated by Django 4.1.4 on 2022-12-30 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_delete_employees_delete_teachers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='student',
            name='lastname',
        ),
    ]
