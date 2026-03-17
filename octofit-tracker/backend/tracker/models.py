from django.db import models


class Team(models.Model):
	name = models.CharField(max_length=120, unique=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name


class UserProfile(models.Model):
	username = models.CharField(max_length=120, unique=True)
	first_name = models.CharField(max_length=120, blank=True)
	last_name = models.CharField(max_length=120, blank=True)
	email = models.EmailField(unique=True)
	fitness_level = models.CharField(max_length=40, default="beginner")
	team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.username


class Activity(models.Model):
	ACTIVITY_TYPES = [
		("running", "Running"),
		("walking", "Walking"),
		("strength", "Strength"),
	]

	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="activities")
	activity_type = models.CharField(max_length=32, choices=ACTIVITY_TYPES)
	duration_minutes = models.PositiveIntegerField()
	calories_burned = models.PositiveIntegerField(default=0)
	points = models.PositiveIntegerField(default=0)
	date = models.DateField()

	def __str__(self):
		return f"{self.user.username} - {self.activity_type}"


class WorkoutSuggestion(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="workouts")
	title = models.CharField(max_length=120)
	description = models.TextField()
	difficulty = models.CharField(max_length=32, default="easy")
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username} - {self.title}"


class LeaderboardEntry(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="leaderboard_entries")
	team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
	total_points = models.PositiveIntegerField(default=0)
	rank = models.PositiveIntegerField(default=0)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["rank", "-total_points"]

	def __str__(self):
		return f"{self.rank}: {self.user.username} ({self.total_points})"
