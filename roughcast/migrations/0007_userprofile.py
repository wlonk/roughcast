# Generated by Django 3.0.7 on 2020-08-23 20:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import roughcast.models

IN_APP = 1
IN_APP_INSTANT_EMAIL = 3


def forwards(apps, schema_editor):
    User = apps.get_model("roughcast", "User")
    UserProfile = apps.get_model("roughcast", "UserProfile")

    for user in User.objects.filter(profile__isnull=True):
        UserProfile.objects.create(user=user)


def backwards(apps, schema_editor):
    pass



class Migration(migrations.Migration):

    dependencies = [
        ("roughcast", "0006_alphatestemail"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="profile",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("bio", models.TextField(blank=True)),
                (
                    "notif_comments",
                    models.PositiveSmallIntegerField(
                        default=IN_APP,
                        validators=[django.core.validators.MaxValueValidator(7)],
                    ),
                ),
                (
                    "notif_mentions",
                    models.PositiveSmallIntegerField(
                        default=IN_APP,
                        validators=[django.core.validators.MaxValueValidator(7)],
                    ),
                ),
                (
                    "notif_versions",
                    models.PositiveSmallIntegerField(
                        default=IN_APP_INSTANT_EMAIL,
                        validators=[django.core.validators.MaxValueValidator(7)],
                    ),
                ),
                (
                    "notif_games",
                    models.PositiveSmallIntegerField(
                        default=IN_APP_INSTANT_EMAIL,
                        validators=[django.core.validators.MaxValueValidator(7)],
                    ),
                ),
            ],
        ),
        migrations.RunPython(forwards, backwards),
    ]