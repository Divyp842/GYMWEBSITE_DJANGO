# Generated by Django 5.1.7 on 2025-03-18 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0011_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Selectdate', models.DateTimeField(auto_now_add=True)),
                ('phonenumber', models.CharField(max_length=15)),
                ('Login', models.CharField(max_length=200)),
                ('Logout', models.CharField(max_length=200)),
                ('SelectWorkout', models.CharField(max_length=200)),
                ('TrainedBy', models.CharField(max_length=200)),
            ],
        ),
    ]
