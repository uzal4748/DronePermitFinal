from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import auth
# Create your views here.
def signin(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect("http://localhost:8000/admin/")
            elif user is not None and user.is_user:
                login(request, user)
                return redirect('user')
            elif user is not None and user.is_officer:
                login(request, user)
                return redirect('officer')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request,'signin.html', {'form': form, 'msg': msg})

def signup(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('signin')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form': form, 'msg': msg})

def user_view(request):
    return render(request,'index.html')

def officer_view(request):
    return redirect('permit')

def logout(request): # Logout
    auth.logout(request)
    return render(request, 'index.html')

