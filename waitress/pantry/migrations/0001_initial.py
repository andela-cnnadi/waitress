# Generated by Django 2.2.9 on 2020-03-04 00:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("app", "0010_delete_pantry")]

    operations = [
        migrations.CreateModel(
            name="Pantry",
            fields=[
                (
                    "id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.SlackUser"
                    ),
                ),
            ],
        )
    ]