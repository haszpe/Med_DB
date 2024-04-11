from django.db import models


class Employees(models.Model):

    first_name = models.CharField(max_length=100)
    sec_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name


class Laboratory(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)


class Project(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)


class Results(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)


class Experiments(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)


class KeyWords(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)


class Protocols(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)


class Patients(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
