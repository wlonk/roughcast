from django.contrib import admin

from .models import Game, Publisher, PublisherMembership, User, Version

admin.site.register(User)
admin.site.register(Publisher)
admin.site.register(PublisherMembership)
admin.site.register(Game)
admin.site.register(Version)
