# Generated by Django 3.2.3 on 2021-05-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sample", "0015_auto_20210423_0935"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.TextField(unique=True)),
            ],
        ),
    ]
