from django.db import models


class Laboratory(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)


class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    sec_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    employee_login = models.CharField(max_length=100)
    employee_password = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    pesel = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)


class Project(models.Model):
    project_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    teamleader_employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)


class Experiments(models.Model):
    experiment_name = models.CharField(max_length=50)
    start_date = models.DateField()
    status = models.CharField(max_length=100)
    end_date = models.DateField()
    results_description = models.CharField(max_length=100, null=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)


class Results(models.Model):
    filename = models.CharField(max_length=50)
    experiment_id = models.ForeignKey(Experiments, on_delete=models.CASCADE)


class KeyWords(models.Model):
    key_word = models.CharField(max_length=50)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    experiment_id = models.ForeignKey(Experiments, on_delete=models.CASCADE)


class Protocols(models.Model):
    protocol_name = models.CharField(max_length=50)
    experiment_id = models.ForeignKey(Experiments, on_delete=models.CASCADE)


class Patients(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=[('m', 'male'), ('f', 'female')])
    date_of_birth = models.DateField()
    pesel = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    experiment_id = models.ForeignKey(Experiments, on_delete=models.CASCADE)

