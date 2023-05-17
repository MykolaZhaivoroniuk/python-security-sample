# --- urls.py ---
...
urlpatterns = [
    ...,
    path('generate-pwd-reset-url/', host_header_injection.HostHeaderInjectionView.as_view(), name='host_header_injection_view')
]



# --- view.py ---
# Issue
from django.http import JsonResponse
from app.models import UserModel

def host_header_injection_view(request):
    customer = UserModel.objects.get(email=request.POST.get('email'))
    resetToken = genPwdResetToken(customer._id)
    resetPwdUrl = f"{request.POST.get('host')}/passwordReset?token={resetToken}&id={customer._id}" 
    return JsonResponse({'resetPwdUrl': resetPwdUrl}, status=200)


# Remediation
from django.http import JsonResponse
from app.models import UserModel
from django.conf import settings

def host_header_injection_view(request):
    customer = UserModel.objects.get(email=request.POST.get('email'))
    resetToken = genPwdResetToken(customer._id)
    resetPwdUrl = f"{settings.HOST_URL}/passwordReset?token={resetToken}&id={customer._id}" 
    return JsonResponse({'resetPwdUrl': resetPwdUrl}, status=200)
