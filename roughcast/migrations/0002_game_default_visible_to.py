# Generated by Django 3.0.7 on 2020-08-17 02:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roughcast", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="default_visible_to",
            field=models.ManyToManyField(
                blank=True, related_name="accessible_games", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
