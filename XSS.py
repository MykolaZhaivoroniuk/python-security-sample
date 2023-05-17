# --- urls.py ---
...
urlpatterns = [
    ...,
    path('query_params_demo/', XSSView.as_view(), name='query_params_view')
]



# --- view.py ---
# Issue
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect

def query_params_view(request):
    url = request.GET.get('redirect')
    return redirect(url)


# Remediation
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect

def query_params_view(request):
    url = request.GET.get('redirect')

    # validate url
    if not url:
        return HttpResponseBadRequest('Missing URL parameter')
    if not url.startswith('http://') and not url.startswith('https://'):
        return HttpResponseBadRequest('Invalid URL scheme')
    
    return redirect(url)
