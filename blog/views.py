from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
    return render(request,'blog/base.html')


def blog(request):
    return HttpResponse("hello here i am with a new blog")