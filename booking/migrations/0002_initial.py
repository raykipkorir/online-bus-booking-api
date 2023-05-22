# Generated by Django 4.2 on 2023-05-21 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("inventory", "0001_initial"),
        ("booking", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tripbus",
            name="bus",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="inventory.bus"
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="seat",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="inventory.seat"
            ),
        ),
        migrations.AddField(
            model_name="ticket",
            name="trip_bus",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="booking.tripbus"
            ),
        ),
    ]
