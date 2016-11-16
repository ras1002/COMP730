from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fund(models.Model):
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    owner = models.ForeignKey(User)

    def __str__(self):
        return "{}: {}".format(self.owner, self.balance)

    def deposit(self,amount):
        '''
        Returns false if amount <= 0
        else Adds amount to balance, saves object to DB, returns True
        '''
        if amount <= 0:
            return False
        else:
            self.balance += amount
            self.save()
            return True

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=64)
    fund = models.ForeignKey(Fund)

    def __str__(self):
        return "{}: {}".format(self.fund.owner, self.amount)

    def process(self):
        f = self.fund
        f.balance -= amount
        f.save()
