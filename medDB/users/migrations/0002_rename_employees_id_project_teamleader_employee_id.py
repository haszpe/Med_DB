# Generated by Django 4.1 on 2024-04-25 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="employees_id",
            new_name="teamleader_employee_id",
        ),
    ]
