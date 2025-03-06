from django.contrib import admin
from games.models import Game, GameCategory

admin.site.register(GameCategory)
admin.site.register(Game)
