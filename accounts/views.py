from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_view(request):
    """ Login view """
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {'error': 'invalid username or passord'}
            return render(request, 'accounts/login.html', context=context)
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html', {})


def logout_view(request):
    """ logout view """
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
    context = {}
    return render(request, 'accounts/logout.html', context=context)


def register_view(request):
    """ register view """
    context = {}
    return render(request, 'accounts/register.html', context=context)