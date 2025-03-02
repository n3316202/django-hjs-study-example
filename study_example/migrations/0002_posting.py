# Generated by Django 4.2.19 on 2025-03-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("study_example", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Posting",
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
                (
                    "owner_name",
                    models.CharField(help_text="Name of posting owner", max_length=128),
                ),
                (
                    "contents",
                    models.CharField(help_text="Contents of posting", max_length=32),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, help_text="Creation time"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, help_text="Last modified time"),
                ),
            ],
            options={
                "db_table": "posting",
                "get_latest_by": ("modified_at", "created_at"),
            },
        ),
    ]
