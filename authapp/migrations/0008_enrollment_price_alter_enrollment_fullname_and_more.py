# Generated by Django 5.1.7 on 2025-03-18 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_enrollment_duedate_enrollment_pymentstatus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='price',
            field=models.IntegerField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='Fullname',
            field=models.CharField(default='Fullname', max_length=25),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='pymentStatus',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
