# Generated by Django 2.2 on 2019-11-21 23:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("sample", "0002_library"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
