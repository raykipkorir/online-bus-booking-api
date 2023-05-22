# Generated by Django 4.2 on 2023-05-21 07:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ticket",
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
                    "ticket_number",
                    models.PositiveIntegerField(
                        help_text="Don't share your ticket number",
                        max_length=8,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("cost", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="TripBus",
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
                ("travel_date", models.DateTimeField()),
                ("available_seats", models.PositiveSmallIntegerField()),
            ],
            options={
                "verbose_name_plural": "Trip Bus",
            },
        ),
    ]
