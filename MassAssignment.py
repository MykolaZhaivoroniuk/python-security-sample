# --- urls.py ---
...
urlpatterns = [
    ...,
    path('signup/', MassAssignmentView.as_view(), name='mass_assignment_view')
]



# --- view.py ---
# Issue
from django.http import JsonResponse
from app.models import UserModel
import json

def mass_assignment_view(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    queryset = UserModel.objects.filter(username=username)
    password = request.POST.get('password')

    if queryset.count() == 0:
        UserModel.objects.create(username=username, email=email, pwd=password)
        return JsonResponse({}, status=200)
    else :
        return JsonResponse({}, status=409)


# Remediation
from django.http import JsonResponse
from app.models import UserModel
import json

def mass_assignment_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')

    if type(username) != str:
        return JsonResponse({'msg': 'Invalid username'}, status=400)

    queryset = UserModel.objects.filter(username=username)

    if queryset.count() == 0:
        encryptedPwd = encryptPassword(password)
        UserModel.objects.create(username=username, email=email, pwd=encryptedPwd)
        return JsonResponse({}, status=200)
    else :
        return JsonResponse({}, status=409)

