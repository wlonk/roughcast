from base64 import b64encode
from enum import IntFlag
from os.path import splitext
from random import randint

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from emoji import UNICODE_EMOJI
from rest_framework.authtoken.models import Token

from .fields import StringField
from .model_mixins import BasicModelMixin, SimpleSlugMixin, SubscribableMixin


class Subscribable(models.Model):
    pass


class Subscription(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    subscribable = models.ForeignKey(Subscribable, on_delete=models.CASCADE)


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
        f"{instance.version.game.team.name}/{instance.version.game.name}/"
        f"{instance.version.game.name}-{instance.version.name}-{random_hash}{ext}"
    )


# Used in EmojiReaction:
def is_emoji(value):
    # @@@ TODO: This is simplistic for now:
    return value in UNICODE_EMOJI["en"]


class AlphaTestEmail(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):  # pragma: nocover
        return self.email


class User(AbstractUser):
    token = None  # We only show a token on a user after auth'ing.
    is_email_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)

    def get_or_create_token(self):
        return Token.objects.get_or_create(user=self)[0].key

    def get_full_name(self):
        return self.first_name.strip()

    def __str__(self):
        return f"{self.get_full_name()} (@{self.username})"

    def notify(self, message):
        """
        message: {
            "type": "comments" | "mentions" | "versions" | "games",
            "path": <path on roughcast to relevant data>,
            "subject": <string subject. this is also the short form for in-app>,
            "email_template": <string to the email template to use>,
            "email_context": <dict of additional context to put in email>,
        }
        """
        if "type" in message:
            in_app = self.profile._should_notify(
                message["type"], NotificationPreferences.IN_APP
            )
            instant_email = self.profile._should_notify(
                message["type"], NotificationPreferences.INSTANT_EMAIL
            )
            digest_email = self.profile._should_notify(
                message["type"], NotificationPreferences.DIGEST_EMAIL
            )
            if in_app:
                InAppNotification.objects.create(
                    user=self,
                    notification_type=message.pop("type"),
                    path=message.pop("path"),
                    subject=message.pop("subject"),
                    additional_context=message,
                )
            if instant_email:  # pragma: nocover
                # @TODO: send email right away
                pass
            if digest_email:  # pragma: nocover
                # @TODO: create digest-email model instance.
                # @TODO: run weekly job to scoop up digest emails models and
                # build and send an email.
                pass


class NotificationPreferences(IntFlag):
    NONE = 0
    IN_APP = 1
    INSTANT_EMAIL = 2
    DIGEST_EMAIL = 4


NOTIFICATION_TYPES = (
    ("comments", "comments"),
    ("mentions", "mentions"),
    ("versions", "versions"),
    ("games", "games"),
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="profile"
    )
    notif_comments = models.PositiveSmallIntegerField(
        default=NotificationPreferences.IN_APP,
        validators=[MaxValueValidator(sum(NotificationPreferences))],
    )
    notif_mentions = models.PositiveSmallIntegerField(
        default=NotificationPreferences.IN_APP,
        validators=[MaxValueValidator(sum(NotificationPreferences))],
    )
    notif_versions = models.PositiveSmallIntegerField(
        default=NotificationPreferences.IN_APP | NotificationPreferences.INSTANT_EMAIL,
        validators=[MaxValueValidator(sum(NotificationPreferences))],
    )
    notif_games = models.PositiveSmallIntegerField(
        default=NotificationPreferences.IN_APP | NotificationPreferences.INSTANT_EMAIL,
        validators=[MaxValueValidator(sum(NotificationPreferences))],
    )

    def _should_notify(self, notification_type, notification_method):
        return bool(getattr(self, f"notif_{notification_type}") & notification_method)

    def __str__(self):
        return f"UserProfile for {self.user.username}"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class InAppNotification(BasicModelMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seen_at = models.DateTimeField(null=True, blank=True)
    notification_type = models.CharField(max_length=32, choices=NOTIFICATION_TYPES)
    path = models.CharField(max_length=128)
    additional_context = models.JSONField(blank=True, null=True)
    subject = models.CharField(max_length=128, blank=True)


class DigestEmailElement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(null=True, blank=True)
    notification_type = models.CharField(max_length=32, choices=NOTIFICATION_TYPES)
    path = models.CharField(max_length=128)
    additional_context = models.JSONField(blank=True, null=True)


class Team(SubscribableMixin, BasicModelMixin, SimpleSlugMixin, models.Model):
    name = StringField(unique=True)
    description = models.TextField()
    url = models.URLField(blank=True)

    members = models.ManyToManyField(
        User,
        through="TeamMembership",
        related_name="team_memberships",
    )

    subscribable = models.OneToOneField(Subscribable, on_delete=models.CASCADE)

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=("name",), name="unique_team_name"),
            models.UniqueConstraint(fields=("slug",), name="unique_team_slug"),
        )

    def __str__(self):
        return self.name


class TeamMembership(BasicModelMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} is a member of {self.team.name}"


class TeamInviteQuerySet(models.QuerySet):
    def for_user(self, user):
        return self.filter(
            Q(to_email=user.email) | Q(team__in=user.team_memberships.all())
        )


class TeamInvite(BasicModelMixin, models.Model):
    objects = TeamInviteQuerySet.as_manager()

    to_email = models.EmailField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class Game(SubscribableMixin, BasicModelMixin, SimpleSlugMixin, models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = StringField()
    banner = models.ImageField(null=True, blank=True)
    description = models.TextField()
    default_is_public = models.BooleanField(default=False)

    subscribable = models.OneToOneField(Subscribable, on_delete=models.CASCADE)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("team", "name"),
                name="unique_name_per_team",
            ),
            models.UniqueConstraint(fields=("slug",), name="unique_game_slug"),
        )

    def __str__(self):
        return f"{self.name} by {self.team.name}"


class Version(BasicModelMixin, SimpleSlugMixin, models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = StringField()
    changelog = models.TextField()
    is_public = models.BooleanField(default=False)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("game", "name"),
                name="unique_name_per_game",
            ),
            models.UniqueConstraint(
                fields=("game", "slug"), name="unique_slug_per_game"
            ),
        )
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.game} version {self.name}"

    def get_notification_message(self):
        game = self.game
        team = game.team
        return {
            "type": "versions",
            "path": f"/t/{team.slug}/{game.slug}/{self.slug}",
            "subject": f"Check out {game.name} {self.name}",
            "email_template": "new_version.html",
            "email_context": {
                "team": str(team.id),
                "game": str(game.id),
                "version": str(self.id),
            },
        }

    def save(self, *args, **kwargs):
        ret = super().save(*args, **kwargs)
        message = self.get_notification_message()
        for subscription in self.game.subscribable.subscription_set.all():
            subscription.user.notify(message)
        return ret


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
