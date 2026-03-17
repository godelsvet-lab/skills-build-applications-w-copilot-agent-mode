from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion
from .serializers import (
	ActivitySerializer,
	LeaderboardEntrySerializer,
	TeamSerializer,
	UserProfileSerializer,
	WorkoutSuggestionSerializer,
)


class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
	queryset = UserProfile.objects.select_related('team').all()
	serializer_class = UserProfileSerializer


class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.select_related('user').all()
	serializer_class = ActivitySerializer


class WorkoutSuggestionViewSet(viewsets.ModelViewSet):
	queryset = WorkoutSuggestion.objects.select_related('user').all()
	serializer_class = WorkoutSuggestionSerializer


class LeaderboardEntryViewSet(viewsets.ModelViewSet):
	queryset = LeaderboardEntry.objects.select_related('user', 'team').all()
	serializer_class = LeaderboardEntrySerializer

	@action(detail=False, methods=['get'])
	def recompute(self, _request):
		# Keep leaderboard in sync with activity totals to simplify frontend consumption.
		leaderboard_rows = []
		totals = (
			Activity.objects.values('user')
			.annotate(total_points=Sum('points'))
			.order_by('-total_points')
		)

		rank = 1
		for total in totals:
			user = UserProfile.objects.select_related('team').get(id=total['user'])
			entry, _ = LeaderboardEntry.objects.update_or_create(
				user=user,
				defaults={
					'team': user.team,
					'total_points': total['total_points'] or 0,
					'rank': rank,
				},
			)
			leaderboard_rows.append(entry)
			rank += 1

		serializer = self.get_serializer(leaderboard_rows, many=True)
		return Response(serializer.data)
