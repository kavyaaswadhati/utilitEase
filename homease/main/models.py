from django.db import models
from djangotoolbox.fields import ListField

class House(models.Model):
    name = models.CharField(max_length=50)
	address = models.CharField(max_length=50)

class User(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
    venmo = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

class Bill(model.Model):
    utility = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    utilityusername = models.CharField(max_length=50)
    utilitypassword = models.CharField(max_length=50)
    date = models.DateField()


class Payment(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField()

class Records(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    lastupdate = models.DateField()
