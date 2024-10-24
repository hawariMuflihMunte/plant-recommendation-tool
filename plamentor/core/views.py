from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect

def index(request):
    return render(request, 'core/pages/index.html')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'core/auth/login.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully loggen in.')
            return redirect('core:home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('core:login')

    return redirect('core:login')