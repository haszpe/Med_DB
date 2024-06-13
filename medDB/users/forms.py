from django import forms
from .models import Employees


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AddEmployee(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ("first_name", "sec_name", "surname",
                   "employee_login", "employee_password",
                   "mail", "pesel", "phone_number", "laboratory")
        labels = {
        "first_name": "",
        "sec_name": "",
        "surname": "",
        "employee_login": "",
        "employee_password": "",
        "mail": "",
        "pesel": "",
        "phone_number": "",
        "laboratory": ""}
        widgets = {"first_name": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'First Name'}),
            "sec_name": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Second Name'}),
            "surname": forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Last Name'}),
            "employee_login": forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Account login'}),
            "employee_password": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Account Password'}),
            "mail": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'E-mail adress'}),
            "pesel": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'PESEL number'}),
            "phone_number": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Phone number'}),
            "laboratory": forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Laboratory'})}
