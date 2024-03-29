# Generated by Django 5.0.3 on 2024-03-29 21:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RestaurantWithdrawal",
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
                ("account_bank", models.CharField(blank=True, max_length=200)),
                ("amount", models.IntegerField()),
                ("currency", models.CharField(blank=True, max_length=3)),
                ("narration", models.TextField(blank=True)),
                ("reference", models.CharField(blank=True, max_length=200)),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="restaurant_withdrawal",
                        to="app.restaurant",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="restaurant_user_withdrawal",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
