from django.db import models
from django.contrib.auth.models import User
from decimal import *

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
        amount = Decimal(amount)
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

    def can_process(self):
        '''
        Returns true if there is more money in the fund than the amount of the transaction
        '''
        return self.fund.balance > self.amount

    def process(self):
        '''
        Processes the transaction, actually deducts the money from the fund
        '''
        if self.can_process():
            f = self.fund
            f.balance -= self.amount
            f.save()
            return True
        else:
            return False;
