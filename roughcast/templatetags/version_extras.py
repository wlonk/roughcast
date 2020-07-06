from django import template

register = template.Library()


@register.filter
def reports_for(version, user):
    return version.reports_for_user(user)
