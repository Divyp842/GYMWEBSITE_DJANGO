# Generated by Django 5.1.7 on 2025-03-18 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_rename_fullname_enrollment_fullname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='fullname',
            new_name='Fullname',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='pymentStatus',
            new_name='PymentStatus',
        ),
    ]
