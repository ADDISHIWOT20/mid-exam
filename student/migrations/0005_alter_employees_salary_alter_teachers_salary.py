# Generated by Django 4.1.4 on 2022-12-29 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_employees_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='salary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='salary',
            field=models.IntegerField(),
        ),
    ]