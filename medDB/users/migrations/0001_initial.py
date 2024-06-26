# Generated by Django 4.1 on 2024-04-25 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employees",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("sec_name", models.CharField(max_length=100)),
                ("surname", models.CharField(max_length=100)),
                ("employee_login", models.CharField(max_length=100)),
                ("employee_password", models.CharField(max_length=100)),
                ("mail", models.CharField(max_length=100)),
                ("pesel", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Experiments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("experiment_name", models.CharField(max_length=50)),
                ("start_date", models.DateField()),
                ("status", models.CharField(max_length=100)),
                ("end_date", models.DateField()),
                ("results_description", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Laboratory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("adress", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Results",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("filename", models.CharField(max_length=50)),
                (
                    "experiment_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.experiments",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Protocols",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("protocol_name", models.CharField(max_length=50)),
                (
                    "experiment_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.experiments",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project_name", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=100)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "employees_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.employees",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Patients",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("surname", models.CharField(max_length=50)),
                (
                    "sex",
                    models.CharField(
                        choices=[("m", "male"), ("f", "female")], max_length=1
                    ),
                ),
                ("date_of_birth", models.DateField()),
                ("pesel", models.CharField(max_length=11)),
                ("phone_number", models.CharField(max_length=50)),
                ("mail", models.CharField(max_length=50)),
                ("group", models.CharField(max_length=50)),
                (
                    "experiment_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.experiments",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="KeyWords",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key_word", models.CharField(max_length=50)),
                (
                    "experiment_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.experiments",
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.project"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="experiments",
            name="project_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.project"
            ),
        ),
        migrations.AddField(
            model_name="employees",
            name="laboratory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.laboratory"
            ),
        ),
    ]
