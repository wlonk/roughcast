from base64 import b64encode
from os.path import splitext
from random import randint

from django.contrib.auth.models import AbstractUser
from django.db import models
from emoji import UNICODE_EMOJI
from rest_framework.authtoken.models import Token

from .fields import StringField
from .model_mixins import BasicModelMixin, SimpleSlugMixin


# Used in Version:
def attached_file_upload_to(instance, filename):
    _, ext = splitext(filename)
    # We don't have access to the instance.pk yet, because it's still
    # being saved to the DB, so this will have to do as a way to
    # distinguish likely name collisions.
    random_hash = b64encode(str(randint(100000, 999999)).encode("utf-8")).decode(
        "utf-8"
    )
    return (
        f"{instance.version.game.publisher.name}/{instance.version.game.name}/"
        f"{instance.version.game.name}-{instance.version.name}-{random_hash}{ext}"
    )


# Used in EmojiReaction:
def is_emoji(value):
    # @@@ TODO: This is simplistic for now:
    return value in UNICODE_EMOJI


class User(AbstractUser):
    token = None  # We only show a token on a user after auth'ing.

    def get_or_create_token(self):
        return Token.objects.get_or_create(user=self)[0].key

    def get_full_name(self):
        return self.first_name.strip()

    def __str__(self):
        return f"{self.get_full_name()} (@{self.username})"


class Publisher(BasicModelMixin, SimpleSlugMixin, models.Model):
    name = StringField(unique=True)
    description = models.TextField()
    url = models.URLField(blank=True)

    members = models.ManyToManyField(
        User, through="PublisherMembership", related_name="publisher_memberships",
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=("name",), name="unique_publisher_name"),
            models.UniqueConstraint(fields=("slug",), name="unique_publisher_slug"),
        )

    def __str__(self):
        return self.name


class PublisherMembership(BasicModelMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} is a member of {self.publisher.name}"


class Game(BasicModelMixin, SimpleSlugMixin, models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    name = StringField()
    banner = models.ImageField(null=True, blank=True)
    description = models.TextField()

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("publisher", "name"), name="unique_name_per_publisher",
            ),
            models.UniqueConstraint(fields=("slug",), name="unique_game_slug"),
        )

    def __str__(self):
        return f"{self.name} by {self.publisher.name}"


class Version(BasicModelMixin, SimpleSlugMixin, models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = StringField()
    changelog = models.TextField()
    is_public = models.BooleanField(default=False)
    visible_to = models.ManyToManyField(
        User, related_name="accessible_versions", blank=True
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("game", "name"), name="unique_name_per_game",
            ),
            models.UniqueConstraint(
                fields=("game", "slug"), name="unique_slug_per_game"
            ),
        )
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.game} version {self.name}"


class AttachedFile(BasicModelMixin, models.Model):
    version = models.ForeignKey(Version, on_delete=models.CASCADE)
    attached_file = models.FileField(upload_to=attached_file_upload_to)


# XXX: Here and below unused currently
class PlaytestReport(BasicModelMixin, models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    for_version = models.ForeignKey(Version, on_delete=models.CASCADE)
    is_locked = models.BooleanField(default=False)
    locked_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="+", blank=True
    )
    locked_at = models.DateTimeField(null=True, blank=True)

    # def __str__(self):
    #     return f"{self.for_version} from {self.for_playtestgroup}"


class PlaytestReportComment(BasicModelMixin, models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    playtest_report = models.ForeignKey(PlaytestReport, on_delete=models.CASCADE)
    body = models.TextField()

    # def __str__(self):
    #     return f"Playtest comment from {self.created_by} for {self.playtest_report}"


class EmojiReaction(BasicModelMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(PlaytestReportComment, on_delete=models.CASCADE)
    emoji = StringField(validators=[is_emoji])

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("user", "comment", "emoji"),
                name="unique_emoji_per_user_per_comment",
            ),
        )

    # def __str__(self):
    #     return f"{self.emoji} from {self.user}"
