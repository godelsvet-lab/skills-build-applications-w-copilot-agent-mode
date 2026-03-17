from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class ObjectIdStringSerializerMixin:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'id' in data:
            data['id'] = str(data['id'])
        return data


class TeamSerializer(ObjectIdStringSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class UserProfileSerializer(ObjectIdStringSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ActivitySerializer(ObjectIdStringSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class WorkoutSuggestionSerializer(ObjectIdStringSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = WorkoutSuggestion
        fields = '__all__'


class LeaderboardEntrySerializer(ObjectIdStringSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = LeaderboardEntry
        fields = '__all__'
