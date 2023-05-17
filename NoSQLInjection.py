# --- urls.py ---
...
urlpatterns = [
    ...,
    path('user/', NoSQLInjectionView.as_view(), name='nosql_injection_view')
]



# --- view.py ---
# Issue
from django.http import JsonResponse
from app.models import UserModel
import json

def nosql_injection_view(request):
    username = request.POST.get('username')
    queryset = UserModel.objects.filter(username=username)

    if queryset.count() != 0:
        json_result = json.dumps(list(queryset.values()))
        return JsonResponse(json_result)
    else :
        return JsonResponse({'message': 'There was an error finding user'}, status=500)


# Remediation
from django.http import JsonResponse
from app.models import UserModel
import json

def nosql_injection_view(request):
    username = request.POST.get('username')

    if type(username) != str:
        return JsonResponse({'message': 'Invalid username'}, status=400)

    queryset = UserModel.objects.filter(username=username)

    if queryset.count() != 0:
        json_result = json.dumps(list(queryset.values()))
        return JsonResponse(json_result)
    else :
        return JsonResponse({'message': 'There was an error finding user'}, status=500)