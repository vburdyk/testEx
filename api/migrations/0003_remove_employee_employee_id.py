# Generated by Django 4.2.4 on 2023-08-05 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_id',
        ),
    ]
