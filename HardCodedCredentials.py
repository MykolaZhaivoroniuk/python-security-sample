# --- urls.py ---
...
urlpatterns = [
    ...,
    path('login/', HardCodedCredentialsView.as_view(), name='hard_coded_credentials_view')
]



# --- view.py ---
# Issue
from django.contrib.auth import authenticate
from django.http import JsonResponse
import jwt
secret_key = 'my-super-duper-secret-key'

def generate_jwt_token(user):
    payload = {
        'user': user,
        'exp': datetime.utcnow() + timedelta(days=7),
    }

    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token.decode('utf-8')

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload['user']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def hard_coded_credentials_view(request):
    user = { id: '123', 'name': 'John Doe', 'password': '123' }
    user = authenticate(request, username=user.name, id=user.id, password=user.password)

    if user is not None:
        token = generate_jwt_token(user)
        return JsonResponse({'token': token})
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)


# Remediation
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.conf import settings
import jwt

def generate_jwt_token(user):
    payload = {
        'user': user,
        'exp': datetime.utcnow() + settings.JWT_EXPIRATION_DELTA,
    }

    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return token.decode('utf-8')

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return payload['user']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def hard_coded_credentials_view(request):
    user = { id: '123', 'name': 'John Doe', 'password': '123' }
    user = authenticate(request, username=user.name, id=user.id, password=user.password)

    if user is not None:
        token = generate_jwt_token(user)
        return JsonResponse({'token': token})
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)