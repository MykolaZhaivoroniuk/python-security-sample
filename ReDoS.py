# --- urls.py ---
...
urlpatterns = [
    ...,
    path('validateEmail/', ReDoSView.as_view(), name='redos_view')
]



# --- view.py ---
# Issue
import re
from django.http import JsonResponse

def redos_view(request):
    pattern = re.compile(r'^([a-zA-Z0-9])(([\-.]|[_]+)?([a-zA-Z0-9]+))*(@){1}[a-z0-9]+[.]{1}(([a-z]{2,3})|([a-z]{2,3}[.]{1}[a-z]{2,3}))$')
    email = request.POST.get('email')

    if pattern.match(email):
        return JsonResponse({'valid': True})
    else:
        return JsonResponse({'error': 'Invalid email'}, status=400)



# Remediation
from django.http import JsonResponse
from validate_email import validate_email

def redos_view(request):
    email = request.POST.get('email')

    if validate_email(email):
        return JsonResponse({'valid': True})
    else:
        return JsonResponse({'error': 'Invalid email'}, status=400)
