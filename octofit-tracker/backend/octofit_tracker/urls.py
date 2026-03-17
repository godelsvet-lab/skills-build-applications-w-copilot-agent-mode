"""octofit_tracker URL Configuration."""
import os

from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"


def api_root(_request):
    return JsonResponse(
        {
            'message': 'OctoFit Tracker API',
            'base_url': base_url,
            'endpoints': {
                'users': f'{base_url}/api/users/',
                'teams': f'{base_url}/api/teams/',
                'activities': f'{base_url}/api/activities/',
                'workouts': f'{base_url}/api/workouts/',
                'leaderboard': f'{base_url}/api/leaderboard/',
            },
        }
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include('tracker.urls')),
    path('', api_root, name='root'),
]
