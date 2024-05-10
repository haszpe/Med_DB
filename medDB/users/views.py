from django.shortcuts import render
from django.http import HttpResponse
from .models import Employees

# def welcome_view(request):
#     message = '<h1>Welcome to Users</h1>'
#     return HttpResponse(message)


def french_view(request, *args, **kwargs):
    return render(request, "base.html")


def testing(request):
    all_employees = Employees.objects.all()
    context = {'all_employees': all_employees}

    return render(request, 'base.html', context)
