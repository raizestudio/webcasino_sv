from django.contrib import admin

from users.models import PlayerProfile, User

admin.site.register(User)
admin.site.register(PlayerProfile)
