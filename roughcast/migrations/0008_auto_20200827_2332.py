# Generated by Django 3.1 on 2020-08-27 23:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roughcast", "0007_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.CreateModel(
            name="InAppNotification",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("seen_at", models.DateTimeField(blank=True, null=True)),
                (
                    "notification_type",
                    models.CharField(
                        choices=[
                            ("comments", "comments"),
                            ("mentions", "mentions"),
                            ("versions", "versions"),
                            ("games", "games"),
                        ],
                        max_length=32,
                    ),
                ),
                ("path", models.CharField(max_length=128)),
                ("additional_context", models.JSONField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DigestEmailElement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sent_at", models.DateTimeField(blank=True, null=True)),
                (
                    "notification_type",
                    models.CharField(
                        choices=[
                            ("comments", "comments"),
                            ("mentions", "mentions"),
                            ("versions", "versions"),
                            ("games", "games"),
                        ],
                        max_length=32,
                    ),
                ),
                ("path", models.CharField(max_length=128)),
                ("additional_context", models.JSONField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]