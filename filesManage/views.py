from django.shortcuts import render
from .forms import LoginForm

def index(request):
    loginform = LoginForm()
    context = {
        "loginform": loginform,
        "a": "a"
    }
    return render(request, 'base.html', context)