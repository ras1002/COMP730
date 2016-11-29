from django.db import models
from django.contrib.auth.models import User
from fundTracker.models import Fund, Transaction
import time
# Create your models here.

class Goal(models.Model):
    title = models.CharField(max_length=255)
    goal_amount = models.DecimalField(max_digits=6, decimal_places=2)
    current_saved = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name = "goal_set")

    def __str__(self):
        return self.title + " - " + str(self.owner)

    def is_completed(self):
        '''
        Checks if the goal has been completed
        Returns True if current_saved > goal_amount
        '''
        return self.current_saved > self.goal_amount

    def add_savings(self, user, amount):
        '''
        Adds amount to goals current saved
        Returns false if amount is negative
        '''
        fund = Fund.objects.get(owner=user)
        trans = Transaction(amount=amount, date=time.gmtime(), category="Goal Deposit", fund=fund)
        if amount < 0:
            return False
        else:
            if trans.can_process():
                self.current_saved += amount
                self.save()
            else:
                return False
        return True

    def get_percent_complete(self):
        return int((self.current_saved/self.goal_amount) * 100)
