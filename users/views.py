from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .forms import UserCreateForm
from django.views.decorators.csrf import csrf_exempt
from .jwt_utils import generate_jwt_token

def user(request):
    return render(request, 'users/base.html')
def login(request):
    return render(request,"users/login.html")
def signup(request):
    return render(request,"users/signup.html")
@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():  
            user = form.save()
            return JsonResponse({"message":user})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token = generate_jwt_token(user.id)
            return JsonResponse({'token': token})
        else:
            return JsonResponse({'error': 'Invalid credentials'})

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'})
