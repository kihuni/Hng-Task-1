from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def get_info(request):
    slack_name = request.GET.get('slack_name', None)
    track = request.GET.get('track', None)

    if not slack_name or not track:
        return JsonResponse({
            "error": "Missing slack_name or track parameters."
        }, status=400)

    current_utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    response_data = {
        "slack_name": slack_name,
        "current_day": datetime.utcnow().strftime('%A'),
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": "https://github.com/kihuni/myproject/blob/main/myproject/myapp/views.py",
        "github_repo_url": "https://github.com/kihuni/myproject",
        "status_code": 200
    }

    return JsonResponse(response_data)
