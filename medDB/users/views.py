from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.http import HttpResponse
# for users listing
from .models import Employees
from django.shortcuts import render

def first_page(request):
    return render(request, 'first_page.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    message = "<h1>Welcome to the app of Medical Data Base!</h1>"
    return HttpResponse(message)


def user_logout(request):
    logout(request)
    return redirect('login')

def list_employee(request):
    all_employees = Employees.objects.all()
    context = {'all_employees': all_employees}  # Create context dictionary
    return render(request, 'list_employee.html', context)
