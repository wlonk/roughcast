from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core import signing
from django.template.loader import render_to_string
from django_registration.exceptions import ActivationError


# Sending:
def _get_activation_key(user):
    """
    Generate the activation key which will be emailed to the user.
    """
    return signing.dumps(obj=user.get_username(), salt=settings.REGISTRATION_SALT)


def _get_email_context(request, activation_key):
    """
    Build the template context used for the activation email.
    """
    scheme = "https" if request.is_secure() else "http"
    return {
        "scheme": scheme,
        "activation_key": activation_key,
        "expiration_days": settings.ACCOUNT_ACTIVATION_DAYS,
        "site": get_current_site(request),
    }


def send_activation_email(user, request):
    """
    Send the activation email. The activation key is the username,
    signed using TimestampSigner.
    """
    email_body_template = "django_registration/activation_email_body.txt"
    email_subject_template = "django_registration/activation_email_subject.txt"

    activation_key = _get_activation_key(user)
    context = _get_email_context(request, activation_key)
    context["user"] = user
    subject = render_to_string(
        template_name=email_subject_template,
        context=context,
        request=request,
    )
    # Force subject to a single line to avoid header-injection
    # issues.
    subject = "".join(subject.splitlines())
    message = render_to_string(
        template_name=email_body_template,
        context=context,
        request=request,
    )
    user.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)


# Activation:
def _validate_key(activation_key):
    """
    Verify that the activation key is valid and within the
    permitted activation time window, returning the username if
    valid or raising ``ActivationError`` if not.
    """
    try:
        username = signing.loads(
            activation_key,
            salt=settings.REGISTRATION_SALT,
            max_age=settings.ACCOUNT_ACTIVATION_DAYS * 86400,
        )
        return username
    except signing.SignatureExpired:
        raise ActivationError("Code has expired.", code="expired")
    except signing.BadSignature:
        raise ActivationError(
            "Code is invalid.",
            code="invalid_key",
            params={"activation_key": activation_key},
        )


def _get_user(username):
    """
    Given the verified username, look up and return the
    corresponding user account if it exists, or raising
    ``ActivationError`` if it doesn't.
    """
    User = get_user_model()
    try:
        user = User.objects.get(**{User.USERNAME_FIELD: username})
        if user.is_email_verified:
            raise ActivationError(
                "This email is already verified.", code="already_activated"
            )
        return user
    except User.DoesNotExist:
        raise ActivationError("No matching user found.", code="bad_username")


def activate(activation_key):
    username = _validate_key(activation_key)
    user = _get_user(username)
    user.is_email_verified = True
    user.save()
    return user
