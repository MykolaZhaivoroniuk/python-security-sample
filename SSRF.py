# --- urls.py ---
...
urlpatterns = [
    ...,
    path('api/data', SSFRView.as_view(), name='ssfr_view')
]


# --- view.py ---
# Issue
import requests
from django.http import JsonResponse

def ssfr_view(request):
    url = request.GET.get('url')
    try:
        response = requests.get(url)
        return JsonResponse(response.json())
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


# Remediation
import requests
from django.http import JsonResponse

def ssfr_view(request):
    url = request.GET.get('url')
    allowedUrls = ['https://example.com/countries.json',
                'https://example.com/states.json']

    if not url:
        return JsonResponse({'error': 'Missing URL parameter'}, status=400)
    if not url.startswith('http://') and not url.startswith('https://'):
        return JsonResponse({'error': 'Invalid URL scheme'}, status=400)
    if not url in allowedUrls:
        return JsonResponse({'error': 'Not allowed'}, status=400)

    try:
        response = requests.get(url)
        return JsonResponse(response.json())
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


