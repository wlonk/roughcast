from django.contrib import admin

from .models import Game, Team, TeamMembership, User, Version

admin.site.register(User)
admin.site.register(Team)
admin.site.register(TeamMembership)
admin.site.register(Game)
admin.site.register(Version)
