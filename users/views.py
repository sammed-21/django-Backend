from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from .jwt_utils import generate_jwt_token
# Create your views here

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_Valid():
            user= form.save()
            return JsonResponse({"message":"User registered successfully"})
        else:
            return JsonResponse({'error': 'Invalid registration data'}, status=400)
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            token = generate_jwt_token(user.id)
            return JsonResponse({'token':token})
        else:
            return JsonResponse({'error':'invalid credentials'})

def logout_view(request):
    logout(request)
    return JsonResponse({'message':'logged out successful'})