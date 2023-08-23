from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path('blog',views.blog)
]
