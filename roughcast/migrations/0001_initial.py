# Generated by Django 3.0.7 on 2020-08-12 04:21

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import hashid_field.field
from django.conf import settings
from django.db import migrations, models

import roughcast.fields
import roughcast.models
import roughcast.slugs

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text=(
                            "Designates that this user has all permissions without "
                            "explicitly assigning them."
                        ),
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text=(
                            "Required. 150 characters or fewer. Letters, digits and "
                            "@/./+/-/_ only."
                        ),
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text=(
                            "Designates whether the user can log into this admin site."
                        ),
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text=(
                            "Designates whether this user should be treated as active. "
                            "Unselect this instead of deleting accounts."
                        ),
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text=(
                            "The groups this user belongs to. A user will get all "
                            "permissions granted to each of their groups."
                        ),
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", django.contrib.auth.models.UserManager())],
        ),
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    hashid_field.field.HashidAutoField(
                        alphabet=ALPHABET,
                        min_length=7,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("edited_at", models.DateTimeField(auto_now=True)),
                ("slug", roughcast.slugs.CustomSlugField(blank=True, max_length=255)),
                ("name", roughcast.fields.StringField()),
                ("banner", models.ImageField(blank=True, null=True, upload_to="")),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="PlaytestReport",
            fields=[
                (
                    "id",
                    hashid_field.field.HashidAutoField(
                        alphabet=ALPHABET,
                        min_length=7,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("edited_at", models.DateTimeField(auto_now=True)),
                ("is_locked", models.BooleanField(default=False)),
                ("locked_at", models.DateTimeField(blank=True, null=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="Publisher",
            fields=[
                (
                    "id",
                    hashid_field.field.HashidAutoField(
                        alphabet=ALPHABET,
                        min_length=7,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("edited_at", models.DateTimeField(auto_now=True)),
                ("slug", roughcast.slugs.CustomSlugField(blank=True, max_length=255)),
                ("name", roughcast.fields.StringField(unique=True)),
                ("description", models.TextField()),
                ("url", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    hashid_field.field.HashidAutoField(
                        alphabet=ALPHABET,
                        min_length=7,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("edited_at", models.DateTimeField(auto_now=True)),
                ("slug", roughcast.slugs.CustomSlugField(blank=True, max_length=255)),
                ("name", roughcast.fields.StringField()),
                ("changelog", models.TextField()),
                ("is_public", models.BooleanField(default=False)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "game",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="roughcast.Game"
                    ),
                ),
                (
                    "visible_to",
                    models.ManyToManyField(
                        blank=True,
                        related_name="accessible_versions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ("-created_at",)},
        ),
        migrations.CreateModel(
            name="PublisherMembership",
            fields=[
                (
                    "id",
                    hashid_field.field.HashidAutoField(
                        alphabet=ALPHABET,
                        min_length=7,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("edited_at", models.DateTimeField(auto_now=True)),
                ("is_owner", models.BooleanField(default=False)),
                (
                    "publisher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="roughcast.Publisher",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="publisher",
            name="members",
            field=models.ManyToManyField(
                related_name="publisher_memberships",
                through="roughcast.PublisherMembership",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="PlaytestReportComment",
            fields=[
                (
                    "id",
                    hashid_field.field.HashidAutoField(
                        alphabet=ALPHABET,
                        min_length=7,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("edited_at", models.DateTimeField(auto_now=True)),
                ("body", models.TextField()),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "playtest_report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="roughcast.PlaytestReport",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddField(
            model_name="playtestreport",
            name="for_version",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="roughcast.Version"
            ),
        ),
        migrations.AddField(
            model_name="playtestreport",
            name="locked_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="game",
            name="publisher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="roughcast.Publisher"
            ),
        ),
        migrations.CreateModel(
            name="EmojiReaction",
            fields=[
                (
                    "id",
                    hashid_field.field.HashidAutoField(
                        alphabet=ALPHABET,
                        min_length=7,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("edited_at", models.DateTimeField(auto_now=True)),
                (
                    "emoji",
                    roughcast.fields.StringField(
                        validators=[roughcast.models.is_emoji]
                    ),
                ),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="roughcast.PlaytestReportComment",
                    ),
                ),
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
            name="AttachedFile",
            fields=[
                (
                    "id",
                    hashid_field.field.HashidAutoField(
                        alphabet=ALPHABET,
                        min_length=7,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("edited_at", models.DateTimeField(auto_now=True)),
                (
                    "attached_file",
                    models.FileField(
                        upload_to=roughcast.models.attached_file_upload_to
                    ),
                ),
                (
                    "version",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="roughcast.Version",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.AddConstraint(
            model_name="version",
            constraint=models.UniqueConstraint(
                fields=("game", "name"), name="unique_name_per_game"
            ),
        ),
        migrations.AddConstraint(
            model_name="version",
            constraint=models.UniqueConstraint(
                fields=("game", "slug"), name="unique_slug_per_game"
            ),
        ),
        migrations.AddConstraint(
            model_name="publisher",
            constraint=models.UniqueConstraint(
                fields=("name",), name="unique_publisher_name"
            ),
        ),
        migrations.AddConstraint(
            model_name="publisher",
            constraint=models.UniqueConstraint(
                fields=("slug",), name="unique_publisher_slug"
            ),
        ),
        migrations.AddConstraint(
            model_name="game",
            constraint=models.UniqueConstraint(
                fields=("publisher", "name"), name="unique_name_per_publisher"
            ),
        ),
        migrations.AddConstraint(
            model_name="game",
            constraint=models.UniqueConstraint(
                fields=("slug",), name="unique_game_slug"
            ),
        ),
        migrations.AddConstraint(
            model_name="emojireaction",
            constraint=models.UniqueConstraint(
                fields=("user", "comment", "emoji"),
                name="unique_emoji_per_user_per_comment",
            ),
        ),
    ]
