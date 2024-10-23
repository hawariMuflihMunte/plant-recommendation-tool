from django.shortcuts import render

def index(request):
    return render(request, 'core/pages/index.html')

def login_view(request):
    return render(request, 'core/auth/login.html')