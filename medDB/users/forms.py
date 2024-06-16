from django import forms
from .models import Laboratory,Employees,Project,Experiments,Results,KeyWords,Protocols, Patients


class AddLaboratory(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = ("name", "adress")
        labels = {
            "name": "",
            "adress": ""
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            "adress": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'})
        }

# class AddEmployee(forms.ModelForm):
#     class Meta:
#         model = Employees
#         fields = ("first_name", "sec_name", "surname",
#                    "employee_login", "employee_password",
#                    "mail", "pesel", "phone_number", "laboratory")
#         labels = {
#         "first_name": "",
#         "sec_name": "",
#         "surname": "",
#         "employee_login": "",
#         "employee_password": "",
#         "mail": "",
#         "pesel": "",
#         "phone_number": "",
#         "laboratory": ""}
#         widgets = {"first_name": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'First Name'}),
#             "sec_name": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Second Name'}),
#             "surname": forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Last Name'}),
#             "employee_login": forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Account login'}),
#             "employee_password": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Account Password'}),
#             "mail": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'E-mail adress'}),
#             "pesel": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'PESEL number'}),
#             "phone_number": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Phone number'}),
#             "laboratory": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Laboratory'})}

class AddProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("project_name", "description", "start_date", "end_date", "teamleader_employee_id")
        labels = {
            "project_name": "",
            "description": "",
            "start_date": "",
            "end_date": "",
            "teamleader_employee_id": ""
        }
        widgets = {
            "project_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Name'}),
            "description": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            "start_date": forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Start Date'}),
            "end_date": forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'End Date'}),
            "teamleader_employee_id": forms.Select(attrs={'class': 'form-control', 'placeholder': 'Team Leader'})
        }

class AddExperiment(forms.ModelForm):
    class Meta:
        model = Experiments
        fields = ("experiment_name", "start_date", "status", "end_date", "results_description", "project_id")
        labels = {
            "experiment_name": "",
            "start_date": "",
            "status": "",
            "end_date": "",
            "results_description": "",
            "project_id": ""
        }
        widgets = {
            "experiment_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Experiment Name'}),
            "start_date": forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Start Date'}),
            "status": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status'}),
            "end_date": forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'End Date'}),
            "results_description": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Results Description'}),
            "project_id": forms.Select(attrs={'class': 'form-control', 'placeholder': 'Project'})
        }

class AddResult(forms.ModelForm):
    class Meta:
        model = Results
        fields = ("filename", "experiment_id")
        labels = {
            "filename": "",
            "experiment_id": ""
        }
        widgets = {
            "filename": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Filename'}),
            "experiment_id": forms.Select(attrs={'class': 'form-control', 'placeholder': 'Experiment'})
        }

class AddKeyWord(forms.ModelForm):
    class Meta:
        model = KeyWords
        fields = ("key_word", "project_id", "experiment_id")
        labels = {
            "key_word": "",
            "project_id": "",
            "experiment_id": ""
        }
        widgets = {
            "key_word": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Key Word'}),
            "project_id": forms.Select(attrs={'class': 'form-control', 'placeholder': 'Project'}),
            "experiment_id": forms.Select(attrs={'class': 'form-control', 'placeholder': 'Experiment'})
        }

class AddProtocol(forms.ModelForm):
    class Meta:
        model = Protocols
        fields = ("protocol_name", "experiment_id")
        labels = {
            "protocol_name": "",
            "experiment_id": ""
        }
        widgets = {
            "protocol_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Protocol Name'}),
            "experiment_id": forms.Select(attrs={'class': 'form-control', 'placeholder': 'Experiment'})
        }

class AddPatient(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ("name", "surname", "sex", "date_of_birth", "pesel", "phone_number", "mail", "group", "experiment_id")
        labels = {
            "name": "",
            "surname": "",
            "sex": "",
            "date_of_birth": "",
            "pesel": "",
            "phone_number": "",
            "mail": "",
            "group": "",
            "experiment_id": ""
        }
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            "surname": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
            "sex": forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sex'}),
            "date_of_birth": forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
            "pesel": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PESEL'}),
            "phone_number": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            "mail": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mail'}),
            "group": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Group'}),
            "experiment_id": forms.Select(attrs={'class': 'form-control', 'placeholder': 'Experiment'})
        }

