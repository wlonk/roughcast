"""
Custom fields brought in from https://github.com/SFDO-Tooling/sfdo-template-helpers/

As that's a project I worked on, and I wrote a lot of this code, and it's open-source
and these are generally useful fields, I thought I'd vendor them in here.
"""

from django.contrib.admin import widgets
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS
from django.db import models


class StringField(models.TextField):
    """ A simple unlimited length string field.

    Django's CharField requires a max_length, and TextField displays a multi-
    line widget, but in Postgres there's no reason to add an arbitrary max
    thanks to the `varlena` storage format. So this is a TextField that
    displays as a single line instead of a multiline TextArea.

    That's all."""


# Make sure StringField has its own mapping in FORMFIELD_FOR_DBFIELD_DEFAULTS
# so that it takes precedence over its base class TextField.
FORMFIELD_FOR_DBFIELD_DEFAULTS[StringField] = {"widget": widgets.AdminTextInputWidget}
