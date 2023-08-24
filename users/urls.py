from django.urls import path
from . import views

urlpatterns = [
    # path('',  user),
    # path('register', register_view, name='register-user'),
     path('login/',views.login , name='login'),
     path('',views.signup , name='login'),
    # path('logout/', logout_view, name='logout'),
    # Other URLs for login, logout, etc.
]