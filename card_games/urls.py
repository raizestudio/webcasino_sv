from card_games.views import DeckViewSet, TexasHoldEmViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"decks", DeckViewSet)
router.register(r"texas_hold_em", TexasHoldEmViewSet)

urlpatterns = router.urls
