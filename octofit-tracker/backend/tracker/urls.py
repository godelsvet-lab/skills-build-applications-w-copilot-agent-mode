from rest_framework.routers import DefaultRouter

from .views import (
    ActivityViewSet,
    LeaderboardEntryViewSet,
    TeamViewSet,
    UserProfileViewSet,
    WorkoutSuggestionViewSet,
)

router = DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'activities', ActivityViewSet, basename='activities')
router.register(r'workouts', WorkoutSuggestionViewSet, basename='workouts')
router.register(r'leaderboard', LeaderboardEntryViewSet, basename='leaderboard')

urlpatterns = router.urls
