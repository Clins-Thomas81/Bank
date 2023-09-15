from django.db import models



# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

class RegistrationForm(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)


class District(models.Model):
    name = models.CharField(max_length=100)
    # Other fields as needed

class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    # Other fields as needed

class AccountType(models.Model):
    name = models.CharField(max_length=100)
    # Other fields as needed

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=10)
    phone_number=models.IntegerField(max_length=15)
    mail_id=models.CharField(max_length=50)
    address=models.CharField(max_length=250)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)

    # Other fields as needed
