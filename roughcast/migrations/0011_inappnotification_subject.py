# Generated by Django 3.1 on 2020-09-13 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("roughcast", "0010_auto_20200829_0420"),
    ]

    operations = [
        migrations.AddField(
            model_name="inappnotification",
            name="subject",
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
