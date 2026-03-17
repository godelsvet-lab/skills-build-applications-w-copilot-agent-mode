from datetime import date, timedelta

from django.core.management.base import BaseCommand

from tracker.models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class Command(BaseCommand):
    help = 'Populate octofit_db with sample records for local development.'

    def handle(self, *args, **options):
        blue, _ = Team.objects.get_or_create(
            name='Blue Sharks', defaults={'description': 'Cardio-focused team'}
        )
        green, _ = Team.objects.get_or_create(
            name='Green Tigers', defaults={'description': 'Strength-focused team'}
        )

        mona, _ = UserProfile.objects.get_or_create(
            username='mona',
            defaults={
                'first_name': 'Mona',
                'last_name': 'Octo',
                'email': 'mona@example.com',
                'team': blue,
                'fitness_level': 'intermediate',
            },
        )
        paul, _ = UserProfile.objects.get_or_create(
            username='paul',
            defaults={
                'first_name': 'Paul',
                'last_name': 'Octo',
                'email': 'paul@example.com',
                'team': green,
                'fitness_level': 'beginner',
            },
        )

        Activity.objects.get_or_create(
            user=mona,
            activity_type='running',
            duration_minutes=35,
            calories_burned=320,
            points=45,
            date=date.today() - timedelta(days=1),
        )
        Activity.objects.get_or_create(
            user=paul,
            activity_type='walking',
            duration_minutes=50,
            calories_burned=260,
            points=30,
            date=date.today() - timedelta(days=2),
        )

        WorkoutSuggestion.objects.get_or_create(
            user=mona,
            title='Interval Sprint Session',
            defaults={
                'description': '5x 400m runs with 2-minute recovery walks.',
                'difficulty': 'medium',
            },
        )
        WorkoutSuggestion.objects.get_or_create(
            user=paul,
            title='Intro Strength Circuit',
            defaults={
                'description': 'Bodyweight squats, pushups, and planks for 20 minutes.',
                'difficulty': 'easy',
            },
        )

        LeaderboardEntry.objects.update_or_create(
            user=mona,
            defaults={'team': mona.team, 'total_points': 45, 'rank': 1},
        )
        LeaderboardEntry.objects.update_or_create(
            user=paul,
            defaults={'team': paul.team, 'total_points': 30, 'rank': 2},
        )

        self.stdout.write(self.style.SUCCESS('Sample OctoFit records created.'))
