# Generated by Django 3.0.8 on 2020-07-17 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymember', '0002_alumni_employee_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='nickname',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
