from django.urls import path
from .views import register_user

urlpatterns = [
    path('register/', register_user, name='register-user'),
     path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # Other URLs for login, logout, etc.
]