from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Laboratory(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)


class EmployeeManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)

class Employees(AbstractUser):
    first_name = models.CharField(max_length=100)
    sec_name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    pesel = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE, blank=True, null=True)
    REQUIRED_FIELDS = ['first_name', 'sec_name', 'surname', 'email',
                       'pesel', 'phone_number']
    objects = EmployeeManager()

    def __str__(self):
        return self.username

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

