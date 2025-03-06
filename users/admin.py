from django.contrib import admin

from users.models import Player, User

admin.site.register(User)
admin.site.register(Player)
