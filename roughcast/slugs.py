import re
import unicodedata

from django.core.validators import RegexValidator, _lazy_re_compile
from django.db import models
from django.utils.functional import keep_lazy_text

slug_re = _lazy_re_compile(r"^[-a-zA-Z0-9_.]+\Z")
validate_slug = RegexValidator(
    slug_re,
    (
        "Enter a valid “slug” consisting of letters, numbers,  underscores, dots, or "
        "hyphens."
    ),
    "invalid",
)


@keep_lazy_text
def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to
    hyphens. Remove characters that aren't alphanumerics, underscores,
    or hyphens. Convert to lowercase. Also strip leading and trailing
    whitespace.

    Taken from Django internals, so we can add `.` to the acceptable
    characters. Since we're often slugging versions, there's good reason
    to keep this character.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    value = re.sub(r"[^\w\s.-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "-", value)


class CustomSlugField(models.SlugField):
    default_validators = [validate_slug]
