from django.contrib import admin

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion

admin.site.register(Team)
admin.site.register(UserProfile)
admin.site.register(Activity)
admin.site.register(WorkoutSuggestion)
admin.site.register(LeaderboardEntry)
