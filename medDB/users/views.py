from django.http import HttpResponseRedirect
from .models import Employees
from django.shortcuts import render, redirect
from .forms import AddLaboratory, AddExperiment, AddKeyWord, AddPatient, AddProject, AddProtocol, AddResult, EmployeeRegistration


def home(request):
    return render(request, 'home.html')


def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeRegistration()
    return render(request, 'register.html', {'form': form})



def list_employee(request):
    search_query = request.GET.get('search', '')
    all_employees = Employees.objects.filter(surname__icontains=search_query)
    context = {'all_employees': all_employees}
    return render(request, 'list_employee.html', context)


def add_laboratory(request):
    submitted = False
    if request.method == 'POST':
        form = AddLaboratory(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_templates/add_laboratory?submitted=True')
    else:
        form = AddLaboratory()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_templates/add_laboratory.html', {'form': form, 'submitted': submitted})


def add_project(request):
    submitted = False
    if request.method == 'POST':
        form = AddProject(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_templates/add_project?submitted=True')
    else:
        form = AddProject()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_templates/add_project.html', {'form': form, 'submitted': submitted})


def add_experiment(request):
    submitted = False
    if request.method == 'POST':
        form = AddExperiment(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_templates/add_experiment?submitted=True')
    else:
        form = AddExperiment()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_templates/add_experiment.html',
                  {'form': form, 'submitted': submitted})


def add_result(request):
    submitted = False
    if request.method == 'POST':
        form = AddResult(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_templates/add_result?submitted=True')
    else:
        form = AddResult()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_templates/add_result.html', {'form': form, 'submitted': submitted})


def add_key_word(request):
    submitted = False
    if request.method == 'POST':
        form = AddKeyWord(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_templates/add_key_word?submitted=True')
    else:
        form = AddKeyWord()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_templates/add_key_word.html', {'form': form, 'submitted': submitted})


def add_protocol(request):
    submitted = False
    if request.method == 'POST':
        form = AddProtocol(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_templates/add_protocol?submitted=True')
    else:
        form = AddProtocol()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_templates/add_protocol.html', {'form': form, 'submitted': submitted})


def add_patient(request):
    submitted = False
    if request.method == 'POST':
        form = AddPatient(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_templates/add_patient?submitted=True')
    else:
        form = AddPatient()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_templates/add_patient.html', {'form': form, 'submitted': submitted})


def add_all(request):
    return render(request, 'add_all.html')